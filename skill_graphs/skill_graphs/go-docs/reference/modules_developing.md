[ ![Go](https://go.dev/images/go-logo-white.svg) ](https://go.dev/)
[ Skip to Main Content ](https://go.dev/doc/modules/developing#main-content)
  * [ Why Go _arrow_drop_down_ ](https://go.dev/doc/modules/developing)
Press Enter to activate/deactivate dropdown
    * [ Case Studies ](https://go.dev/solutions/case-studies)
Common problems companies solve with Go
    * [ Use Cases ](https://go.dev/solutions/use-cases)
Stories about how and why companies use Go
    * [ Security ](https://go.dev/security/)
How Go can help keep you secure by default
  * [ Learn ](https://go.dev/learn/)
Press Enter to activate/deactivate dropdown
  * [ Docs _arrow_drop_down_ ](https://go.dev/doc/modules/developing)
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
  * [ Community _arrow_drop_down_ ](https://go.dev/doc/modules/developing)
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
  * [Why Go _navigate_next_](https://go.dev/doc/modules/developing)
[_navigate_before_ Why Go](https://go.dev/doc/modules/developing)
    * [ Case Studies ](https://go.dev/solutions/case-studies)
    * [ Use Cases ](https://go.dev/solutions/use-cases)
    * [ Security ](https://go.dev/security/)
  * [Learn](https://go.dev/learn/)
  * [Docs _navigate_next_](https://go.dev/doc/modules/developing)
[_navigate_before_ Docs](https://go.dev/doc/modules/developing)
    * [ Go Spec ](https://go.dev/ref/spec)
    * [ Go User Manual ](https://go.dev/doc)
    * [ Standard library ](https://pkg.go.dev/std)
    * [ Release Notes ](https://go.dev/doc/devel/release)
    * [ Effective Go ](https://go.dev/doc/effective_go)
  * [Packages](https://pkg.go.dev)
  * [Community _navigate_next_](https://go.dev/doc/modules/developing)
[_navigate_before_ Community](https://go.dev/doc/modules/developing)
    * [ Recorded Talks ](https://go.dev/talks/)
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
    * [ Go blog ](https://go.dev/blog)
    * [ Go project ](https://go.dev/help)
    * Get connected


# Developing and publishing modules
Table of Contents
---

[Workflow for developing and publishing modules](https://go.dev/doc/modules/developing#workflow)


[Design and development](https://go.dev/doc/modules/developing#design)


[Decentralized publishing](https://go.dev/doc/modules/developing#decentralized)


[Package discovery](https://go.dev/doc/modules/developing#discovery)


[Versioning](https://go.dev/doc/modules/developing#versioning)
|
You can collect related packages into modules, then publish the modules for other developers to use. This topic gives an overview of developing and publishing modules.
To support developing, publishing, and using modules, you use:
  * A **workflow** through which you develop and publish modules, revising them with new versions over time. See [Workflow for developing and publishing modules](https://go.dev/doc/modules/developing#workflow).
  * **Design practices** that help a module’s users understand it and upgrade to new versions in a stable way. See [Design and development](https://go.dev/doc/modules/developing#design).
  * A **decentralized system for publishing** modules and retrieving their code. You make your module available for other developers to use from your own repository and publish with a version number. See [Decentralized publishing](https://go.dev/doc/modules/developing#decentralized).
  * A **package search engine** and documentation browser (pkg.go.dev) at which developers can find your module. See [Package discovery](https://go.dev/doc/modules/developing#discovery).
  * A module **version numbering convention** to communicate expectations of stability and backward compatibility to developers using your module. See [Versioning](https://go.dev/doc/modules/developing#versioning).
  * **Go tools** that make it easier for other developers to manage dependencies, including getting your module’s source, upgrading, and so on. See [Managing dependencies](https://go.dev/doc/modules/managing-dependencies).


**See also**
  * If you’re interested simply in using packages developed by others, this isn’t the topic for you. Instead, see [Managing dependencies](https://go.dev/doc/modules/managing-dependencies).
  * For a tutorial that includes a few module development basics, see [Tutorial: Create a Go module](https://go.dev/doc/tutorial/create-module).


## Workflow for developing and publishing modules[¶](https://go.dev/doc/modules/developing#workflow)
When you want to publish your modules for others, you adopt a few conventions to make using those modules easier.
The following high-level steps are described in more detail in [Module release and versioning workflow](https://go.dev/doc/modules/release-workflow).
  1. Design and code the packages that the module will include.
  2. Commit code to your repository using conventions that ensure it’s available to others via Go tools.
  3. Publish the module to make it discoverable by developers.
  4. Over time, revise the module with versions that use a version numbering convention that signals each version’s stability and backward compatibility.


## Design and development[¶](https://go.dev/doc/modules/developing#design)
Your module will be easier for developers to find and use if the functions and packages in it form a coherent whole. When you’re designing a module’s public API, try to keep its functionality focused and discrete.
Also, designing and developing your module with backward compatibility in mind helps its users upgrade while minimizing churn to their own code. You can use certain techniques in code to avoid releasing a version that breaks backward compatibility. For more about those techniques, see [Keeping your modules compatible](https://go.dev/blog/module-compatibility) on the Go blog.
Before you publish a module, you can reference it on the local file system using the replace directive. This makes it easier to write client code that calls functions in the module while the module is still in development. For more information, see “Coding against an unpublished module” in [Module release and versioning workflow](https://go.dev/doc/modules/release-workflow#unpublished).
## Decentralized publishing[¶](https://go.dev/doc/modules/developing#decentralized)
In Go, you publish your module by tagging its code in your repository to make it available for other developers to use. You don’t need to push your module to a centralized service because Go tools can download your module directly from your repository (located using the module’s path, which is a URL with the scheme omitted) or from a proxy server.
After importing your package in their code, developers use Go tools (including the `go get` command) to download your module’s code to compile with. To support this model, you follow conventions and best practices that make it possible for Go tools (on behalf of another developer) to retrieve your module’s source from your repository. For example, Go tools use the module’s module path you specify, along with the module version number you use to tag the module for release, to locate and download the module for its users.
For more about source and publishing conventions and best practices, see [Managing module source](https://go.dev/doc/modules/managing-source).
For step-by-step instructions on publishing a module, see [Publishing a module](https://go.dev/doc/modules/publishing).
## Package discovery[¶](https://go.dev/doc/modules/developing#discovery)
After you’ve published your module and someone has fetched it with Go tools, it will become visible on the Go package discovery site at [pkg.go.dev](https://pkg.go.dev/). There, developers can search the site to find it and read its documentation.
To begin using the module, a developer imports packages from the module, then runs the `go get` command to download its source code to compile with.
For more about how developers find and use modules, see [Managing dependencies](https://go.dev/doc/modules/managing-dependencies).
## Versioning[¶](https://go.dev/doc/modules/developing#versioning)
As you revise and improve your module over time, you assign version numbers (based on the semantic versioning model) designed to signal each version’s stability and backward compatibility. This helps developers using your module determine when the module is stable and whether an upgrade may include significant changes in behavior. You indicate a module’s version number by tagging the module’s source in the repository with the number.
For more on developing major version updates, see [Developing a major version update](https://go.dev/doc/modules/major-version).
For more about how you use the semantic versioning model for Go modules, see [Module version numbering](https://go.dev/doc/modules/version-numbers).
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
