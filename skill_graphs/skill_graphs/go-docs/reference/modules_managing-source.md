[ ![Go](https://go.dev/images/go-logo-white.svg) ](https://go.dev/)
[ Skip to Main Content ](https://go.dev/doc/modules/managing-source#main-content)
  * [ Why Go _arrow_drop_down_ ](https://go.dev/doc/modules/managing-source)
Press Enter to activate/deactivate dropdown
    * [ Case Studies ](https://go.dev/solutions/case-studies)
Common problems companies solve with Go
    * [ Use Cases ](https://go.dev/solutions/use-cases)
Stories about how and why companies use Go
    * [ Security ](https://go.dev/security/)
How Go can help keep you secure by default
  * [ Learn ](https://go.dev/learn/)
Press Enter to activate/deactivate dropdown
  * [ Docs _arrow_drop_down_ ](https://go.dev/doc/modules/managing-source)
Press Enter to activate/deactivate dropdown
    * [ Go Spec ](https://go.dev/ref/spec)
The official Go language specification
    * [ Go User Manual ](https://go.dev/doc)
A complete introduction to building software with Go
    * [ Standard library ](https://pkg.go.dev/std)
Reference documentation for Go's standard library
    * [ Release Notes ](https://go.dev/doc/devel/release)
Learn what's new in each Go release
    * [ Effective Go ](https://go.dev/doc/effective_go)
Tips for writing clear, performant, and idiomatic Go code
  * [ Packages ](https://pkg.go.dev)
Press Enter to activate/deactivate dropdown
  * [ Community _arrow_drop_down_ ](https://go.dev/doc/modules/managing-source)
Press Enter to activate/deactivate dropdown
    * [ Recorded Talks ](https://go.dev/talks/)
Videos from prior events
    * Meet other local Go developers
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
Learn and network with Go developers from around the world
    * [ Go blog ](https://go.dev/blog)
The Go project's official blog.
    * [ Go project ](https://go.dev/help)
Get help and stay informed from Go
    * Get connected


[ ![Go.](https://go.dev/images/go-logo-blue.svg) ](https://go.dev/)
  * [Why Go _navigate_next_](https://go.dev/doc/modules/managing-source)
[_navigate_before_ Why Go](https://go.dev/doc/modules/managing-source)
    * [ Case Studies ](https://go.dev/solutions/case-studies)
    * [ Use Cases ](https://go.dev/solutions/use-cases)
    * [ Security ](https://go.dev/security/)
  * [Learn](https://go.dev/learn/)
  * [Docs _navigate_next_](https://go.dev/doc/modules/managing-source)
[_navigate_before_ Docs](https://go.dev/doc/modules/managing-source)
    * [ Go Spec ](https://go.dev/ref/spec)
    * [ Go User Manual ](https://go.dev/doc)
    * [ Standard library ](https://pkg.go.dev/std)
    * [ Release Notes ](https://go.dev/doc/devel/release)
    * [ Effective Go ](https://go.dev/doc/effective_go)
  * [Packages](https://pkg.go.dev)
  * [Community _navigate_next_](https://go.dev/doc/modules/managing-source)
[_navigate_before_ Community](https://go.dev/doc/modules/managing-source)
    * [ Recorded Talks ](https://go.dev/talks/)
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
    * [ Go blog ](https://go.dev/blog)
    * [ Go project ](https://go.dev/help)
    * Get connected


# Managing module source
Table of Contents
---

[How Go tools find your published module](https://go.dev/doc/modules/managing-source#tools)


[Organizing code in the repository](https://go.dev/doc/modules/managing-source#repository)


[Choosing repository scope](https://go.dev/doc/modules/managing-source#repository-scope)
    [Sourcing one module per repository](https://go.dev/doc/modules/managing-source#one-module-source)     [Sourcing multiple modules in a single repository](https://go.dev/doc/modules/managing-source#multiple-module-source) |
When you’re developing modules to publish for others to use, you can help ensure that your modules are easier for other developers to use by following the repository conventions described in this topic.
This topic describes actions you might take when managing your module repository. For information about the sequence of workflow steps you’d take when revising from version to version, see [Module release and versioning workflow](https://go.dev/doc/modules/release-workflow).
Some of the conventions described here are required in modules, while others are best practices. This content assumes you’re familiar with the basic module use practices described in [Managing dependencies](https://go.dev/doc/modules/managing-dependencies).
Go supports the following repositories for publishing modules: Git, Subversion, Mercurial, Bazaar, and Fossil.
For an overview of module development, see [Developing and publishing modules](https://go.dev/doc/modules/developing).
## How Go tools find your published module[¶](https://go.dev/doc/modules/managing-source#tools)
In Go’s decentralized system for publishing modules and retrieving their code, you can publish your module while leaving the code in your repository. Go tools rely on naming rules that have repository paths and repository tags indicating a module’s name and version number. When your repository follows these requirements, your module code is downloadable from your repository by Go tools such as the [`go get` command](https://go.dev/ref/mod#go-get).
When a developer uses the `go get` command to get source code for packages their code imports, the command does the following:
  1. From `import` statements in Go source code, `go get` identifies the module path within the package path.
  2. Using a URL derived from the module path, the command locates the module source on a module proxy server or at its repository directly.
  3. Locates source for the module version to download by matching the module’s version number to a repository tag to discover the code in the repository. When a version number to use is not yet known, `go get` locates the latest release version.
  4. Retrieves module source and downloads it to the developer’s local module cache.


## Organizing code in the repository[¶](https://go.dev/doc/modules/managing-source#repository)
You can keep maintenance simple and improve developers’ experience with your module by following the conventions described here. Getting your module code into a repository is generally as simple as with other code.
The following diagram illustrates a source hierarchy for a simple module with two packages.
![Diagram illustrating a module source code hierarchy](https://go.dev/doc/modules/images/source-hierarchy.png)
Your initial commit should include files listed in the following table:
File  | Description
---|---
LICENSE | The module's license.
go.mod |  Describes the module, including its module path (in effect, its name) and its dependencies. For more, see the [go.mod reference](https://go.dev/doc/modules/gomod-ref). The module path will be given in a module directive, such as: ```
module example.com/mymodule
```
For more about choosing a module path, see [Managing dependencies](https://go.dev/doc/modules/managing-dependencies#naming_module). Though you can edit the go.mod file, you'll find it more reliable to make changes through `go` commands.
go.sum |  Contains cryptographic hashes that represent the module's dependencies. Go tools use these hashes to authenticate downloaded modules, attempting to confirm that the downloaded module is authentic. Where this confirmation fails, Go will display a security error. The file will be empty or not present when there are no dependencies. You shouldn't edit this file except by using the `go mod tidy` command, which removes unneeded entries.
Package directories and .go sources. | Directories and .go files that comprise the Go packages and sources in the module.
From the command-line, you can create an empty repository, add the files that will be part of your initial commit, and commit with a message. Here’s an example using git:
```
$ git init
$ git add --all
$ git commit -m "mycode: initial commit"
$ git push

```

## Choosing repository scope[¶](https://go.dev/doc/modules/managing-source#repository-scope)
You publish code in a module when the code should be versioned independently from code in other modules.
Designing your repository so that it hosts a single module at its root directory will help keep maintenance simpler, particularly over time as you publish new minor and patch versions, branch into new major versions, and so on. However, if your needs require it, you can instead maintain a collection of modules in a single repository.
### Sourcing one module per repository[¶](https://go.dev/doc/modules/managing-source#one-module-source)
You can maintain a repository that has a single module’s source in it. In this model, you place your go.mod file at the repository root, with package subdirectories containing Go source beneath.
This is the simplest approach, making your module likely easier to manage over time. It helps you avoid the need to prefix a module version number with a directory path.
![Diagram illustrating a single module's source in its repository](https://go.dev/doc/modules/images/single-module.png)
### Sourcing multiple modules in a single repository[¶](https://go.dev/doc/modules/managing-source#multiple-module-source)
You can publish multiple modules from a single repository. For example, you might have code in a single repository that constitutes multiple modules, but want to version those modules separately.
Each subdirectory that is a module root directory must have its own go.mod file.
Sourcing module code in subdirectories changes the form of the version tag you must use when publishing a module. You must prefix the version number part of the tag with the name of the subdirectory that is the module root. For more about version numbers, see [Module version numbering](https://go.dev/doc/modules/version-numbers).
For example, for module `example.com/mymodules/module1` below, you would have the following for version v1.2.3:
  * Module path: `example.com/mymodules/module1`
  * Version tag: `module1/v1.2.3`
  * Package path imported by a user: `example.com/mymodules/module1/package1`
  * Module path and version as specified in a user’s require directive: `example.com/mymodules/module1 v1.2.3`


![Diagram illustrating two modules in a single repository](https://go.dev/doc/modules/images/multiple-modules.png)
[ Why Go ](https://go.dev/solutions/) [ Use Cases ](https://go.dev/solutions/use-cases) [ Case Studies ](https://go.dev/solutions/case-studies)
[ Get Started ](https://go.dev/learn/) [ Playground ](https://go.dev/play) [ Tour ](https://go.dev/tour/) [ Help ](https://go.dev/help/)
[ Packages ](https://pkg.go.dev) [ Standard Library ](https://go.dev/pkg/) [ About Go Packages ](https://pkg.go.dev/about)
[ About ](https://go.dev/project) [ Download ](https://go.dev/dl/) [ Blog ](https://go.dev/blog/) [ Release Notes ](https://go.dev/doc/devel/release) [ Brand Guidelines ](https://go.dev/brand) [ Code of Conduct ](https://go.dev/conduct)
Opens in new window.
![The Go Gopher](https://go.dev/images/gophers/pilot-bust.svg)
  * [Copyright](https://go.dev/copyright)
  * [Terms of Service](https://go.dev/tos)
  * [ Report an Issue ](https://go.dev/s/website-issue)
  * ![System theme](https://go.dev/images/icons/brightness_6_gm_grey_24dp.svg) ![Dark theme](https://go.dev/images/icons/brightness_2_gm_grey_24dp.svg) ![Light theme](https://go.dev/images/icons/light_mode_gm_grey_24dp.svg)


go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic.
Okay
