[Skip to main content](https://developer.hashicorp.com/terraform/migrate/authenticate#main)
[HashiConf 2025 Don't miss the live stream of HashiConf Day 2 happening now View live stream](https://www.hashicorp.com/conferences/hashiconf#livestream)
Sign In[Sign Up](https://developer.hashicorp.com/sign-up)
Theme
Dark Light System
[Terraform Home](https://developer.hashicorp.com/terraform)
## Terraform Migrate
  * [Terraform Migrate](https://developer.hashicorp.com/terraform/migrate)
  * [Install](https://developer.hashicorp.com/terraform/migrate/install)
  * [Authenticate](https://developer.hashicorp.com/terraform/migrate/authenticate)
  * [Migrate to StacksBETA](https://developer.hashicorp.com/terraform/migrate/stacks)
  * Reference
  * Release notes


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
  3. [Terraform Migrate](https://developer.hashicorp.com/terraform/migrate)
  4. Authenticate


v2.0.x (latest)
  * Terraform Migrate
  * [v1.2.x](https://developer.hashicorp.com/terraform/migrate/v1.2.x)
  * [v1.1.x](https://developer.hashicorp.com/terraform/migrate/v1.1.x)
  * [v1.0.x](https://developer.hashicorp.com/terraform/migrate/v1.0.x)


# Authenticate tf-migrate
To use `tf-migrate`, you must authenticate with HCP Terraform or the Terraform Enterprise instance that you are migrating your state to.
##  [](https://developer.hashicorp.com/terraform/migrate/authenticate#connect-to-hcp-terraform-or-enterprise-terraform)Connect to HCP Terraform or Enterprise Terraform
The `tf-migrate` tool uses your locally configured Terraform CLI API token. If you have not authenticated your local Terraform installation with HCP Terraform, use the `terraform login` command to create an authentication token.
```
$ terraform login

Terraform will request an API token for app.terraform.io using your browser.

If login is successful, Terraform will store the token in plain text in
the following file for use by subsequent commands:
   /Users/redacted/.terraform.d/credentials.tfrc.json

Do you want to proceed?
 Only 'yes' will be accepted to confirm.

 Enter a value: yes
```
```
$ terraform login
 
Terraform will request an API token for app.terraform.io using your browser.
 
If login is successful, Terraform will store the token in plain text in
the following file for use by subsequent commands:
   /Users/redacted/.terraform.d/credentials.tfrc.json
 
Do you want to proceed?
 Only 'yes' will be accepted to confirm.
 
 Enter a value: yes

```

Terraform opens a browser to the HCP Terraform sign in screen, where you can then enter a token name in the web UI, or leave the default name. Click **Create API token** to generate the authentication token.
HCP Terraform only displays your token once. Copy this token, then when the Terraform CLI prompts you, paste the user token exactly once into your terminal. Press **Enter** to complete the authentication process.
##  [](https://developer.hashicorp.com/terraform/migrate/authenticate#authenticate-your-vcs-provider)Authenticate your VCS provider
`tf-migrate` can optionally create a pull request that updates the state storage location specified in your Terraform configuration. To do this, `tf-migrate` uses your VCS provider's API, and requires an API token with permissions to modify your Git repository.
To configure your API token, set the `TF_GIT_PAT_TOKEN` environment variable
```
$ export TF_GIT_PAT_TOKEN=<TOKEN>
```
```
$ export TF_GIT_PAT_TOKEN=<TOKEN>

```

###  [](https://developer.hashicorp.com/terraform/migrate/authenticate#github-connection-requirements)GitHub connection requirements
If your Terraform files are stored in GitHub, you must configure an API token that meets the following requirements:
  * The token must be a classic token. Refer to the
  * The token must have the `repo` OAuth scope.


###  [](https://developer.hashicorp.com/terraform/migrate/authenticate#gitlab-connection-requirements)GitLab connection requirements
If your Terraform files are stored in GitLab Cloud, you must configure an API token that meets the following requirements:
  * The token must be a personal access token. Refer to the
  * The token must have `read_repository` and `write_repository` scopes.


###  [](https://developer.hashicorp.com/terraform/migrate/authenticate#bitbucket-connection-requirements)Bitbucket connection requirements
If your Terraform files are stored in Bitbucket Cloud, you must configure an API token that meets the following requirements:
  * The token must be a repository access token. Refer to the
  * The token must have `repository:write` and `pullrequest:write` scopes.


On this page:
  1. [Authenticate tf-migrate](https://developer.hashicorp.com/terraform/migrate/authenticate#authenticate-tf-migrate)
  2. [Connect to HCP Terraform or Enterprise Terraform](https://developer.hashicorp.com/terraform/migrate/authenticate#connect-to-hcp-terraform-or-enterprise-terraform)
  3. [Authenticate your VCS provider](https://developer.hashicorp.com/terraform/migrate/authenticate#authenticate-your-vcs-provider)


Authenticate `tf-migrate` | Terraform | HashiCorp Developer
