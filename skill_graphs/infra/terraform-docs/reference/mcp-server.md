[Skip to main content](https://developer.hashicorp.com/terraform/mcp-server/prompt#main)
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
## Terraform MCP Server
  * [Terraform MCP Server](https://developer.hashicorp.com/terraform/mcp-server)
  * [Deploy](https://developer.hashicorp.com/terraform/mcp-server/deploy)
  * [Prompt](https://developer.hashicorp.com/terraform/mcp-server/prompt)
  * [Security](https://developer.hashicorp.com/terraform/mcp-server/security)
  * [Reference](https://developer.hashicorp.com/terraform/mcp-server/reference)


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
  3. [Terraform MCP Server](https://developer.hashicorp.com/terraform/mcp-server)
  4. Prompt


v0.4.x (latest)
  * Terraform MCP Server
  * [v0.3.x](https://developer.hashicorp.com/terraform/mcp-server/v0.3.x)


# Prompt a model connected to the Terraform MCP server
This topic provides example prompts for helping you write Terraform configuration after installing the Terraform model context protocol (MCP) server. Refer to [Deploy the Terraform MCP server](https://developer.hashicorp.com/terraform/docs/tools/mcp-server/deploy) for instructions on how to deploy the server.
##  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#overview)Overview
To trigger the MCP server tools, ask your LLM questions about your provider configuration or general questions about Terraform providers and modules. Note that for your LLM to use the server, your questions must pertain to provider configuration from the registry. The LLM uses other sources, such as content from the internet, to respond to general questions about Terraform configuration or requests to generate code.
##  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#requirements)Requirements
Verify that you have deployed the Terraform MCP server and configured your client. Refer to [Deploy the Terraform MCP server](https://developer.hashicorp.com/terraform/docs/tools/mcp-server/deploy) for instructions.
##  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#prompt-your-mcp-client)Prompt your MCP client
Your model may still decide to use other resources to formulate responses, but you can use the following guidelines to help you create prompts that are more likely to be routed through the server:
  * Include the names of specific providers or provider modules. For example, use `google_compute_disk` in your prompt instead of `the compute disk`.
  * Use the full Terraform resource address in your query. Refer to [Resource Address Reference](https://developer.hashicorp.com/terraform/cli/state/resource-addressing) in the Terraform CLI documentation for additional information about resource addresses.
  * Ask for the latest information about the provider or module.


##  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#examples)Examples
You can use the following set of prompts as a guide to help you write your own configuration. The following responses are returned from the server using ChatGPT 4.1 in GitHub Copilot on VS Code. Your responses may vary.
###  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#get-ai-related-resources-from-the-google-provider)Get AI-related resources from the Google provider
In the following example, the server obtains a list of Google provider document IDs so that you can decide which resources to create:
####  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#prompt)Prompt
```
I need help understanding what resources are available
in the Google provider that are for AI
```
```
I need help understanding what resources are available
in the Google provider that are for AI

```

####  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#request)Request
The server sends the following request payload to the registry:
```
{
  "provider_Data_Type": "resources",
  "provider_Name": "google",
  "provider_Namespace": "hashicorp",
  "providerVersion": "latest",
  "serviceSlug": "ai"
}

```
```
{
  "provider_Data_Type": "resources",
  "provider_Name": "google",
  "provider_Namespace": "hashicorp",
  "providerVersion": "latest",
  "serviceSlug": "ai"
}

```

####  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#response)Response
```
The Google Terraform provider offers several resources related to AI, primarily under the Vertex AI and Document AI services. Here are the main AI-related resources available:

**Vertex AI Resources**

- `vertex_ai_dataset`
- `vertex_ai_deployment_resource_pool`
- `vertex_ai_endpoint`
- `vertex_ai_endpoint_iam`
- `vertex_ai_feature_group`
- `vertex_ai_featurestore`
- `vertex_ai_index`
- `vertex_ai_metadata_store`
- `vertex_ai_tensorboard`
- `document_ai_processor`
- `document_ai_warehouse_document_schema`

These resources allow you to manage datasets, endpoints, feature stores, indexes, metadata, and more for AI/ML workflows on Google Cloud, as well as Document AI processors and schemas.
```
```
The Google Terraform provider offers several resources related to AI, primarily under the Vertex AI and Document AI services. Here are the main AI-related resources available:
 
**Vertex AI Resources**
 
- `vertex_ai_dataset`
- `vertex_ai_deployment_resource_pool`
- `vertex_ai_endpoint`
- `vertex_ai_endpoint_iam`
- `vertex_ai_feature_group`
- `vertex_ai_featurestore`
- `vertex_ai_index`
- `vertex_ai_metadata_store`
- `vertex_ai_tensorboard`
- `document_ai_processor`
- `document_ai_warehouse_document_schema`

These resources allow you to manage datasets, endpoints, feature stores, indexes, metadata, and more for AI/ML workflows on Google Cloud, as well as Document AI processors and schemas.

```

###  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#get-information-about-storage-buckets-in-azure)Get information about storage buckets in Azure
The following prompt gets a list of provider documentation IDs. Then, it calls the appropriate documentation for the use case:
```
I need help setting up storage buckets in the azure provider
```
```
I need help setting up storage buckets in the azure provider

```

####  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#request-1)Request
The server sends the following request payloads to the registry:
```
{
  "providerDataType": "resources",
  "providerName": "azurerm",
  "providerNamespace": "hashicorp",
  "providerVersion": "latest",
  "serviceSlug": "storage_account"
}

```
```
{
  "providerDataType": "resources",
  "providerName": "azurerm",
  "providerNamespace": "hashicorp",
  "providerVersion": "latest",
  "serviceSlug": "storage_account"
}

```

```
{
  "providerDocID": "8957547"
}

```
```
{
  "providerDocID": "8957547"
}

```

```
{
  "providerDocID": "8957555"
}

```
```
{
  "providerDocID": "8957555"
}

```

####  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#response-1)Response
The server retrieves several responses from each tool, including example configurations from the registry. The following response is one of the examples:
```
Available Documentation (top matches) for resources in Terraform provider hashicorp/azurerm version: 4.29.0

# azurerm_storage_account

Manages an Azure Storage Account.

## Example Usage

```hcl
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}

resource "azurerm_storage_account" "example" {
  name                     = "storageaccountname"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  tags = {
    environment = "staging"
  }
}
```

To set up storage buckets in Azure using the Terraform azurerm provider, you need to use the azurerm_storage_account resource. Here’s a quick guide and example configuration:

1. Terraform Resource for Azure Storage Account

```hcl
 resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}

resource "azurerm_storage_account" "example" {
  name                     = "storageaccountname" # must be globally unique, lowercase
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"           # or "Premium"
  account_replication_type = "GRS"                # or "LRS", "RAGRS", "ZRS", etc.

  tags = {
   environment = "staging"
  }
}
```
```
```
Available Documentation (top matches) for resources in Terraform provider hashicorp/azurerm version: 4.29.0
 
# azurerm_storage_account
 
Manages an Azure Storage Account.
 
## Example Usage
 
```hcl
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}
 
resource "azurerm_storage_account" "example" {
  name                     = "storageaccountname"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
 
  tags = {
    environment = "staging"
  }
}
```
 
To set up storage buckets in Azure using the Terraform azurerm provider, you need to use the azurerm_storage_account resource. Here’s a quick guide and example configuration:
 
1. Terraform Resource for Azure Storage Account

```hcl
 resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}
 
resource "azurerm_storage_account" "example" {
  name                     = "storageaccountname" # must be globally unique, lowercase
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"           # or "Premium"
  account_replication_type = "GRS"                # or "LRS", "RAGRS", "ZRS", etc.
 
  tags = {
   environment = "staging"
  }
}
```

```

###  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#get-help-creating-an-ibm-vm)Get help creating an IBM VM
The following prompt gets a list of modules:
```
Is there a module to help with setting up an IBM VM?
```
```
Is there a module to help with setting up an IBM VM?

```

####  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#request-2)Request
The server sends the following request payload:
```
{
  "moduleQuery": "ibm vm"
}

```
```
{
  "moduleQuery": "ibm vm"
}

```

####  [](https://developer.hashicorp.com/terraform/mcp-server/prompt#response-2)Response
The client prints the following response using the context acquired from the MCP server:
```
Yes, there is a Terraform module to help with setting up an IBM VM:

- IBM VM Module
- ID: intel/ibm-vm/intel/1.2.2
- Description: Intel Cloud Optimization Module - IBM VM
- Module Version: 1.2.2
- Namespace: intel
- Source: GitHub - intel/terraform-intel-ibm-vm

You can use this module to set up and manage IBM VMs with Terraform.

If you need more details or usage examples, let me know.
```
```
Yes, there is a Terraform module to help with setting up an IBM VM:
 
- IBM VM Module
- ID: intel/ibm-vm/intel/1.2.2
- Description: Intel Cloud Optimization Module - IBM VM
- Module Version: 1.2.2
- Namespace: intel
- Source: GitHub - intel/terraform-intel-ibm-vm
 
You can use this module to set up and manage IBM VMs with Terraform.
 
If you need more details or usage examples, let me know.

```

On this page:
  1. [Prompt a model connected to the Terraform MCP server](https://developer.hashicorp.com/terraform/mcp-server/prompt#prompt-a-model-connected-to-the-terraform-mcp-server)
  2. [Overview](https://developer.hashicorp.com/terraform/mcp-server/prompt#overview)
  3. [Requirements](https://developer.hashicorp.com/terraform/mcp-server/prompt#requirements)
  4. [Prompt your MCP client](https://developer.hashicorp.com/terraform/mcp-server/prompt#prompt-your-mcp-client)
  5. [Examples](https://developer.hashicorp.com/terraform/mcp-server/prompt#examples)


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


Prompt an AI model connected to the Terraform MCP server | Terraform | HashiCorp Developer
