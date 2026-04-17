[Skip to main content](https://developer.hashicorp.com/terraform/plugin/terraform-plugin-protocol#main)
[HashiConf 2025 Don't miss the live stream of HashiConf Day 2 happening now View live stream](https://www.hashicorp.com/conferences/hashiconf#livestream)
Sign In[Sign Up](https://developer.hashicorp.com/sign-up)
Theme
Dark Light System
[Terraform Home](https://developer.hashicorp.com/terraform)
## Plugin Development
  * [Plugin Development](https://developer.hashicorp.com/terraform/plugin)
  * [How Terraform Works With Plugins](https://developer.hashicorp.com/terraform/plugin/how-terraform-works)
  * [Terraform Plugin Protocol](https://developer.hashicorp.com/terraform/plugin/terraform-plugin-protocol)
  * [Framework Benefits](https://developer.hashicorp.com/terraform/plugin/framework-benefits)
  * [Publishing to the Registry](https://developer.hashicorp.com/terraform/registry/providers/publishing)
  * [Terraform Integration Program](https://developer.hashicorp.com/terraform/docs/partnerships)
  * [Debugging](https://developer.hashicorp.com/terraform/plugin/debugging)
  * Best Practices
  * ### Plugin SDKs and Libraries
  * [SDKv2](https://developer.hashicorp.com/terraform/plugin/sdkv2)
  * [Framework](https://developer.hashicorp.com/terraform/plugin/framework)
  * [Logging](https://developer.hashicorp.com/terraform/plugin/log)
  * [Combining and Translating](https://developer.hashicorp.com/terraform/plugin/mux)
  * [Testing](https://developer.hashicorp.com/terraform/plugin/testing)
  * Code Generation


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
  3. [Plugin Development](https://developer.hashicorp.com/terraform/plugin)
  4. Terraform Plugin Protocol


# Terraform plugin protocol
The Terraform plugin protocol is a versioned interface between Terraform CLI and Terraform Plugins.
During [discovery](https://developer.hashicorp.com/terraform/plugin/how-terraform-works#discovery), the Terraform Registry uses the protocol version as additional compatibility metadata when deciding which plugin versions Terraform CLI can select. You can configure this metadata in the [Terraform Registry manifest file](https://developer.hashicorp.com/terraform/registry/providers/publishing#terraform-registry-manifest-file) when you create a plugin release.
Major versions of the protocol delineate Terraform CLI and Terraform Plugin compatibility. Minor versions of the protocol are additive. The protocol is implemented in
For more detail about how the protocol RPCs are used, refer to the following topics:
  * [Framework documentation about RPCs](https://developer.hashicorp.com/terraform/plugin/framework/internals/rpcs)


##  [](https://developer.hashicorp.com/terraform/plugin/terraform-plugin-protocol#protocol-version-6)Protocol Version 6
Protocol version 6 is compatible with Terraform CLI version 1.0 and later. Protocol version 6 includes all version 5 functionality for providers, plus:
  * **Nested Attributes** : Define `SchemaAttribute` with the `NestedType` field.
    * Enable practitioners to use easier [argument syntax](https://developer.hashicorp.com/terraform/language/syntax/configuration#arguments) instead of [block syntax](https://developer.hashicorp.com/terraform/language/syntax/configuration#blocks).
    * Configure value sensitivity on individual nested attributes, rather than an entire read-only (`Computed` only) attribute.


Implementations include:
  * [terraform-plugin-framework](https://developer.hashicorp.com/terraform/plugin/framework): A higher-level SDK that makes Terraform provider development easier by abstracting implementation details.
  * [tf5to6server](https://developer.hashicorp.com/terraform/plugin/mux/translating-protocol-version-5-to-6): A package to translate protocol version 5 providers into protocol version 6.
  * [tf6muxserver](https://developer.hashicorp.com/terraform/plugin/mux/combining-protocol-version-6-providers): A package to combine multiple protocol version 6 providers.


Refer to
##  [](https://developer.hashicorp.com/terraform/plugin/terraform-plugin-protocol#protocol-version-5)Protocol Version 5
Protocol version 5 is compatible with Terraform CLI version 0.12 and later.
Implementations include:
  * [terraform-plugin-framework](https://developer.hashicorp.com/terraform/plugin/framework): A higher-level SDK that makes Terraform provider development easier by abstracting implementation details.
  * [terraform-plugin-sdk/v2](https://developer.hashicorp.com/terraform/plugin/sdkv2): A higher-level SDK that makes Terraform provider development easier by abstracting implementation details.
  * [tf6to5server](https://developer.hashicorp.com/terraform/plugin/mux/translating-protocol-version-6-to-5): A package to translate protocol version 6 providers into protocol version 5.
  * [tf5muxserver](https://developer.hashicorp.com/terraform/plugin/mux/combining-protocol-version-5-providers): A package to combine multiple protocol version 5 providers.


Refer to
On this page:
  1. [Terraform plugin protocol](https://developer.hashicorp.com/terraform/plugin/terraform-plugin-protocol#terraform-plugin-protocol)
  2. [Protocol Version 6](https://developer.hashicorp.com/terraform/plugin/terraform-plugin-protocol#protocol-version-6)
  3. [Protocol Version 5](https://developer.hashicorp.com/terraform/plugin/terraform-plugin-protocol#protocol-version-5)


Terraform plugin protocol | Terraform | HashiCorp Developer
