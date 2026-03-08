[Skip to main content](https://developer.hashicorp.com/terraform/language/providers#main)
[HashiConf 2025 Don't miss the live stream of HashiConf Day 2 happening now View live stream](https://www.hashicorp.com/conferences/hashiconf#livestream)
HashiCorp Cloud Platform
Get started in minutes with our cloud products
[All HCP Products](https://developer.hashicorp.com/hcp)
  * Infrastructure Lifecycle Management
    * [ TerraformManage infrastructure as code ](https://developer.hashicorp.com/terraform)
    * [ PackerBuild machine images ](https://developer.hashicorp.com/packer)
    * [ NomadOrchestrate workloads ](https://developer.hashicorp.com/nomad)
    * [ WaypointStandardize application patterns ](https://developer.hashicorp.com/waypoint)
    * [ VagrantBuild developer environments ](https://developer.hashicorp.com/vagrant)
  * Security Lifecycle Management
    * [ VaultCentrally manage secrets ](https://developer.hashicorp.com/vault)
    * [ BoundarySecure remote access ](https://developer.hashicorp.com/boundary)
    * [ HCP Vault RadarScan for embedded secrets ](https://developer.hashicorp.com/hcp/docs/vault-radar)
    * [ ConsulSecure network services ](https://developer.hashicorp.com/consul)


Learn
  * [ CertificationsGet HashiCorp certified ](https://developer.hashicorp.com/certifications)
  * [ TutorialsLearn HashiCorp products ](https://developer.hashicorp.com/tutorials)
  * [ Validated PatternsField-tested patterns for using HashiCorp products ](https://developer.hashicorp.com/validated-patterns)
  * [ Well-Architected FrameworkAdopt HashiCorp best practices ](https://developer.hashicorp.com/well-architected-framework)


[Terraform](https://developer.hashicorp.com/terraform)
  * [Install](https://developer.hashicorp.com/terraform/install)
  * [Tutorials](https://developer.hashicorp.com/terraform/tutorials)
  * Documentation
    * [Documentation](https://developer.hashicorp.com/terraform/docs)
    * [Intro to Terraform](https://developer.hashicorp.com/terraform/intro)
    * [Configuration Language](https://developer.hashicorp.com/terraform/language)
    * [Terraform CLI](https://developer.hashicorp.com/terraform/cli)
    * [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs)
    * [Terraform Enterprise](https://developer.hashicorp.com/terraform/enterprise)
    * [ Terraform MCP Server BETA ](https://developer.hashicorp.com/terraform/mcp-server)
    * [Terraform Migrate](https://developer.hashicorp.com/terraform/migrate)
    * [Provider Use](https://developer.hashicorp.com/terraform/language/providers)
    * [Plugin Development](https://developer.hashicorp.com/terraform/plugin)
    * [Registry Publishing](https://developer.hashicorp.com/terraform/registry)
    * [Integration Program](https://developer.hashicorp.com/terraform/docs/partnerships)
  * Sandbox
  * (opens in new tab)
  * (opens in new tab)


Search
⌘/ctrl
Command or control key
K
K key
  * Sign in
  * [Sign up](https://developer.hashicorp.com/sign-up)
  * * * *
  * Theme
Dark Light System


Sign In[Sign Up](https://developer.hashicorp.com/sign-up)
Theme
Dark Light System
[Terraform Home](https://developer.hashicorp.com/terraform)
## Configuration Language
  * [Configuration Language](https://developer.hashicorp.com/terraform/language)
  * [Get started](https://developer.hashicorp.com/terraform/tutorials)(opens in new tab)
  * Configure providers
  * Resources
  * Data sources
  * Variables
  * Locals
  * Outputs
  * Modules
  * [Meta-arguments](https://developer.hashicorp.com/terraform/language/meta-arguments)
  * Sensitive data
  * Backends
  * Search and import
  * State
  * Stacks
  * Test and validate
  * Extend CRUD operations
  * * * *
  * ### UPGRADE
  * [Upgrade to v1.14](https://developer.hashicorp.com/terraform/language/upgrade-guides)
  * [v1.x compatibility promises](https://developer.hashicorp.com/terraform/language/v1-compatibility-promises)
  * * * *
  * ### REFERENCE
  * [Style guide](https://developer.hashicorp.com/terraform/language/style)
  * Syntax
  * Files and configuration structure
  * Configuration blocks
  * Stack blocks
  * Query blocks
  * Meta-arguments
  * Built-in resources
  * Expressions
  * Functions
  * [Internals](https://developer.hashicorp.com/terraform/internals)


* * *
  * ### Resources
  * [Tutorial Library](https://developer.hashicorp.com/tutorials/library?product=terraform)
  * [Certifications](https://developer.hashicorp.com/certifications/infrastructure-automation)
  * [Sandbox](https://developer.hashicorp.com/terraform/sandbox)
  * [Community Forum](https://discuss.hashicorp.com/c/terraform-core/27)(opens in new tab)
  * [Support](https://www.hashicorp.com/customer-success)(opens in new tab)
  * (opens in new tab)
  * (opens in new tab)


  1. [Developer](https://developer.hashicorp.com/)
  2. [Terraform](https://developer.hashicorp.com/terraform)
  3. [Configuration Language](https://developer.hashicorp.com/terraform/language)
  4. Configure providers


v1.14.x (latest)
  * Terraform
  * [v1.15.x (alpha)](https://developer.hashicorp.com/terraform/language/v1.15.x/providers)
  * [v1.13.x](https://developer.hashicorp.com/terraform/language/v1.13.x/providers)
  * [v1.12.x](https://developer.hashicorp.com/terraform/language/v1.12.x/providers)
  * [v1.11.x](https://developer.hashicorp.com/terraform/language/v1.11.x/providers)
  * [v1.10.x](https://developer.hashicorp.com/terraform/language/v1.10.x/providers)
  * [v1.9.x](https://developer.hashicorp.com/terraform/language/v1.9.x/providers)
  * [v1.8.x](https://developer.hashicorp.com/terraform/language/v1.8.x/providers)
  * [v1.7.x](https://developer.hashicorp.com/terraform/language/v1.7.x/providers)
  * [v1.6.x](https://developer.hashicorp.com/terraform/language/v1.6.x/providers)
  * [v1.5.x](https://developer.hashicorp.com/terraform/language/v1.5.x/providers)
  * [v1.4.x](https://developer.hashicorp.com/terraform/language/v1.4.x/providers)
  * [v1.3.x](https://developer.hashicorp.com/terraform/language/v1.3.x/providers)
  * [v1.2.x](https://developer.hashicorp.com/terraform/language/v1.2.x/providers)
  * [v1.1.x](https://developer.hashicorp.com/terraform/language/v1.1.x/providers)


# Providers
> **Hands-on:** Try the [Perform CRUD Operations with Providers](https://developer.hashicorp.com/terraform/tutorials/configuration-language/provider-use?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS) tutorial.
Terraform relies on plugins called providers to interact with cloud providers, SaaS providers, and other APIs.
Terraform configurations must declare which providers they require so that Terraform can install and use them. Additionally, some providers require configuration (like endpoint URLs or cloud regions) before they can be used.
##  [](https://developer.hashicorp.com/terraform/language/providers#what-providers-do)What Providers Do
Each provider adds a set of [resource types](https://developer.hashicorp.com/terraform/language/resources) and/or [data sources](https://developer.hashicorp.com/terraform/language/data-sources) that Terraform can manage.
Every resource type is implemented by a provider; without providers, Terraform can't manage any kind of infrastructure.
Most providers configure a specific infrastructure platform (either cloud or self-hosted). Providers can also offer local utilities for tasks like generating random numbers for unique resource names.
##  [](https://developer.hashicorp.com/terraform/language/providers#where-providers-come-from)Where Providers Come From
Providers are distributed separately from Terraform itself, and each provider has its own release cadence and version numbers.
The
##  [](https://developer.hashicorp.com/terraform/language/providers#provider-documentation)Provider Documentation
Each provider has its own documentation, describing its resource types and their arguments.
The
Provider documentation in the Registry is versioned; you can use the version menu in the header to change which version you're viewing.
For details about writing, generating, and previewing provider documentation, see the [provider publishing documentation](https://developer.hashicorp.com/terraform/registry/providers/docs).
##  [](https://developer.hashicorp.com/terraform/language/providers#how-to-use-providers)How to Use Providers
Providers are released separately from Terraform itself and have their own version numbers. In production we recommend constraining the acceptable provider versions in the configuration's provider requirements block, to make sure that `terraform init` does not install newer versions of the provider that are incompatible with the configuration.
To use resources from a given provider, you need to include some information about it in your configuration. See the following pages for details:
  * [Provider Requirements](https://developer.hashicorp.com/terraform/language/providers/requirements) documents how to declare providers so Terraform can install them.
  * [The `provider` block reference](https://developer.hashicorp.com/terraform/language/block/provider) documents how to configure settings for providers.
  * [Dependency Lock File](https://developer.hashicorp.com/terraform/language/files/dependency-lock) documents an additional HCL file that can be included with a configuration, which tells Terraform to always use a specific set of provider versions.


##  [](https://developer.hashicorp.com/terraform/language/providers#provider-installation)Provider Installation
  * HCP Terraform and Terraform Enterprise install providers as part of every run.
  * Terraform CLI finds and installs providers when [initializing a working directory](https://developer.hashicorp.com/terraform/cli/init). It can automatically download providers from a Terraform registry, or load them from a local mirror or cache. If you are using a persistent working directory, you must reinitialize whenever you change a configuration's providers.
To save time and bandwidth, Terraform CLI supports an optional plugin cache. You can enable the cache using the `plugin_cache_dir` setting in [the CLI configuration file](https://developer.hashicorp.com/terraform/cli/config/config-file).


To ensure Terraform always installs the same provider versions for a given configuration, you can use Terraform CLI to create a [dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock) and commit it to version control along with your configuration. If a lock file is present, HCP Terraform, CLI, and Enterprise will all obey it when installing providers.
> **Hands-on:** Try the [Lock and Upgrade Provider Versions](https://developer.hashicorp.com/terraform/tutorials/configuration-language/provider-versioning?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS) tutorial.
###  [](https://developer.hashicorp.com/terraform/language/providers#private-providers)Private Providers
If you are using a provider that is not in a Hashicorp-hosted registry, you may need to attach additional credentials to your requests to external registries. You do not need these credentials if your provider is in the Terraform public registry or the HCP Terraform private registry.
By default, Terraform only authenticates the opening request from a provider to the registry. The registry responds with [follow-up URLs](https://developer.hashicorp.com/terraform/internals/provider-registry-protocol#find-a-provider-package) that Terraform makes requests to, such as telling Terraform to download the provider or the `SHASUMS` file. Hashicorp-hosted registries do not require additional authentication for these follow-up requests. If your registry does require additional credentials for follow-up requests, you can use a `.netrc` file to provide those credentials.
By default, Terraform searches for the `.netrc` file in your `HOME` directory. However, you can override the default filesystem location by setting the `NETRC` environment variable. For information on the format of`.netrc`, refer to the
##  [](https://developer.hashicorp.com/terraform/language/providers#how-to-find-providers)How to Find Providers
To find providers for the infrastructure platforms you use, browse
Some providers on the Registry are developed and published by HashiCorp, some are published by platform maintainers, and some are published by users and volunteers. The provider listings use the following badges to indicate who develops and maintains a given provider.
Tier | Description | Namespace
---|---|---
Official | Official providers are owned and maintained by HashiCorp  | `hashicorp, IBM, IBM-Cloud, ansible`
Partner Premier |  Technology partners are third-party companies that write and maintain partner premier providers. To earn a partner premier badge, the partner must qualify ( [_Refer to the partner premier requirements._](https://developer.hashicorp.com/terraform/docs/partnerships#requirements-for-the-partner-premier-tag)_)_ | Third-party organization
Partner |  Partner providers are written, maintained, validated and published by third-party companies against their own APIs. To earn a partner provider badge the partner must participate in the [_HashiCorp Technology Partner Program_](https://www.hashicorp.com/ecosystem/become-a-partner/) _._ | Third-party organization
Community | Community providers are published to the Terraform Registry by individual maintainers, groups of maintainers, or other members of the Terraform community. | Maintainer’s individual or organization account, e.g. `DeviaVir/gsuite`
Archived | Archived Providers are Official or Partner Providers that are no longer maintained by HashiCorp or the community. This may occur if an API is deprecated or interest was low. |  `hashicorp` or third-party
##  [](https://developer.hashicorp.com/terraform/language/providers#how-to-develop-providers)How to Develop Providers
Providers are written in Go, using the Terraform Plugin SDK. For more information on developing providers, see:
  * The [Plugin Development](https://developer.hashicorp.com/terraform/plugin) documentation
  * The [Call APIs with Terraform Providers](https://developer.hashicorp.com/terraform/tutorials/providers-plugin-framework?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS) tutorials


On this page:
  1. [Providers](https://developer.hashicorp.com/terraform/language/providers#providers)
  2. [What Providers Do](https://developer.hashicorp.com/terraform/language/providers#what-providers-do)
  3. [Where Providers Come From](https://developer.hashicorp.com/terraform/language/providers#where-providers-come-from)
  4. [Provider Documentation](https://developer.hashicorp.com/terraform/language/providers#provider-documentation)
  5. [How to Use Providers](https://developer.hashicorp.com/terraform/language/providers#how-to-use-providers)
  6. [Provider Installation](https://developer.hashicorp.com/terraform/language/providers#provider-installation)
  7. [How to Find Providers](https://developer.hashicorp.com/terraform/language/providers#how-to-find-providers)
  8. [How to Develop Providers](https://developer.hashicorp.com/terraform/language/providers#how-to-develop-providers)


[](https://www.hashicorp.com/)Theme
Dark Light System
  * [Certifications](https://developer.hashicorp.com/certifications)
  * [System Status](https://status.hashicorp.com)
  * Cookie Manager
  * [Terms of Use](https://www.hashicorp.com/terms-of-service)
  * [Security](https://www.hashicorp.com/trust/security)
  * [Privacy](https://www.hashicorp.com/privacy)
  * [Trademark Policy](https://www.hashicorp.com/trademark-policy)
  * [Trade Controls](https://www.hashicorp.com/trade-controls)
  * [Accessibility](https://www.hashicorp.com/trust/accessibility)
  * (opens in new tab)
  * stdin is not a tty
