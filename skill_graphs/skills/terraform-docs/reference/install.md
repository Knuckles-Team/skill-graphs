[Skip to main content](https://developer.hashicorp.com/terraform/install#main)
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
## Install Terraform
  * Install Terraform
  * * * *
  * ### Operating Systems
  * [macOS](https://developer.hashicorp.com/terraform/install#darwin)
  * [Windows](https://developer.hashicorp.com/terraform/install#windows)
  * [Linux](https://developer.hashicorp.com/terraform/install#linux)
  * [FreeBSD](https://developer.hashicorp.com/terraform/install#freebsd)
  * [OpenBSD](https://developer.hashicorp.com/terraform/install#openbsd)
  * [Solaris](https://developer.hashicorp.com/terraform/install#solaris)
  * * * *
  * [Release information](https://developer.hashicorp.com/terraform/install#release-information)
  * [Next steps](https://developer.hashicorp.com/terraform/install#next-steps)


  * * * *
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


# Install Terraform
1.14.6 (latest) 1.13.5 1.12.2 1.11.4 1.10.5 1.9.8 1.8.5 1.7.5 1.6.6 1.5.7 1.4.7 1.3.10 1.2.9 1.1.9 1.0.11
## macOS
[](https://developer.hashicorp.com/terraform/install#darwin)
### Package manager
```
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```
```
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

```

### Binary download
AMD64
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_darwin_amd64.zip)
ARM64
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_darwin_arm64.zip)
## Windows
[](https://developer.hashicorp.com/terraform/install#windows)
### Binary download
386
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_windows_386.zip)
AMD64
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_windows_amd64.zip)
## Linux
[](https://developer.hashicorp.com/terraform/install#linux)
### Package manager
Ubuntu/DebianCentOS/RHELFedora 41Fedora 42Amazon LinuxHomebrew
```
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```
```
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform

```

```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install terraform
```
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install terraform

```

```
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager addrepo --from-repofile=https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
sudo dnf -y install terraform
```
```
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager addrepo --from-repofile=https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
sudo dnf -y install terraform

```

```
wget -O- https://rpm.releases.hashicorp.com/fedora/hashicorp.repo | sudo tee /etc/yum.repos.d/hashicorp.repo
sudo yum list available | grep hashicorp
sudo dnf -y install terraform
```
```
wget -O- https://rpm.releases.hashicorp.com/fedora/hashicorp.repo | sudo tee /etc/yum.repos.d/hashicorp.repo
sudo yum list available | grep hashicorp
sudo dnf -y install terraform

```

```
sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum install terraform
```
```
sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum install terraform

```

```
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```
```
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

```

### Binary download
386
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_linux_386.zip)
AMD64
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_linux_amd64.zip)
ARM
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_linux_arm.zip)
ARM64
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_linux_arm64.zip)
Note
Complete this [tutorial](https://developer.hashicorp.com/well-architected-framework/operational-excellence/verify-hashicorp-binary) to learn how to install and verify HashiCorp tools on any Linux distribution, and create a custom Linux container with verified HashiCorp tools.
## FreeBSD
[](https://developer.hashicorp.com/terraform/install#freebsd)
### Binary download
386
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_freebsd_386.zip)
AMD64
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_freebsd_amd64.zip)
ARM
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_freebsd_arm.zip)
## OpenBSD
[](https://developer.hashicorp.com/terraform/install#openbsd)
### Binary download
386
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_openbsd_386.zip)
AMD64
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_openbsd_amd64.zip)
## Solaris
[](https://developer.hashicorp.com/terraform/install#solaris)
### Binary download
AMD64
Version: 1.14.6
[Download](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_solaris_amd64.zip)
## Release information
[](https://developer.hashicorp.com/terraform/install#release-information)
Changelog
Terraform Version: 1.14.6
(opens in new tab)
Official releases
All officially supported HashiCorp release channels and their security guarantees.
[View all](https://www.hashicorp.com/official-release-channels)(opens in new tab)
Note
You can find the [SHA256 checksums for Terraform 1.14.6](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_SHA256SUMS) online and you can [verify the checksums signature file](https://releases.hashicorp.com/terraform/1.14.6/terraform_1.14.6_SHA256SUMS.sig) which has been signed using [HashiCorp's GPG key](https://www.hashicorp.com/security). Complete this [tutorial](https://developer.hashicorp.com/well-architected-framework/operational-excellence/verify-hashicorp-binary) to learn how to install and verify HashiCorp tools on any Linux distribution.
## Next steps
[](https://developer.hashicorp.com/terraform/install#next-steps)
  * [](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)
6 tutorials
Get Started - AWS
Create, manage, and destroy AWS infrastructure using Terraform. Step-by-step, command-line tutorials will walk you through the Terraform basics for the first time.
    * Terraform
  * [](https://developer.hashicorp.com/terraform/tutorials/azure-get-started)
8 tutorials
Get Started - Azure
Build, change, and destroy Azure infrastructure using Terraform. Step-by-step, command-line tutorials will walk you through the Terraform basics for the first time.
    * Terraform
  * [](https://developer.hashicorp.com/terraform/tutorials/docker-get-started)
7 tutorials
Get Started - Docker
Build, change, and destroy Docker infrastructure using Terraform. Step-by-step, command-line tutorials will walk you through the Terraform basics for the first time.
    * Terraform
  * [](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started)
7 tutorials
Get Started - Google Cloud
Build, change, and destroy Google Cloud Platform (GCP) infrastructure using Terraform. Step-by-step, command-line tutorials will walk you through the Terraform basics for the first time.
    * Terraform
  * [](https://developer.hashicorp.com/terraform/tutorials/oci-get-started)
7 tutorials
Get Started - OCI
Build, change, and destroy a virtual cloud network and subnet on Oracle Cloud Infrastructure (OCI) using Terraform. Step-by-step, command-line tutorials will walk you through the Terraform basics for the first time.
    * Terraform
  * [](https://developer.hashicorp.com/terraform/tutorials/cloud-get-started)
6 tutorials
Get Started - HCP Terraform
Collaborate on version-controlled configuration using HCP Terraform. Follow this track to build, change, and destroy infrastructure using remote runs and state.
    * Terraform


About Terraform
Define cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share.
Featured docs
  * [Introduction to Terraform](https://developer.hashicorp.com/terraform/intro)
  * [Configuration Language](https://developer.hashicorp.com/terraform/language)
  * [Terraform CLI](https://developer.hashicorp.com/terraform/cli/commands)
  * [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs)
  * [Provider Use](https://developer.hashicorp.com/terraform/language/providers)


HCP Terraform
Automate your infrastructure provisioning at any scale
Try HCP Terraform for free
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


Install | Terraform | HashiCorp Developer
