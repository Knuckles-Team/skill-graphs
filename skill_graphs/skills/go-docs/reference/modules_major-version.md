[ ![Go](https://go.dev/images/go-logo-white.svg) ](https://go.dev/)
[ Skip to Main Content ](https://go.dev/doc/modules/major-version#main-content)
  * [ Why Go _arrow_drop_down_ ](https://go.dev/doc/modules/major-version)
Press Enter to activate/deactivate dropdown
    * [ Case Studies ](https://go.dev/solutions/case-studies)
Common problems companies solve with Go
    * [ Use Cases ](https://go.dev/solutions/use-cases)
Stories about how and why companies use Go
    * [ Security ](https://go.dev/security/)
How Go can help keep you secure by default
  * [ Learn ](https://go.dev/learn/)
Press Enter to activate/deactivate dropdown
  * [ Docs _arrow_drop_down_ ](https://go.dev/doc/modules/major-version)
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
  * [ Community _arrow_drop_down_ ](https://go.dev/doc/modules/major-version)
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
  * [Why Go _navigate_next_](https://go.dev/doc/modules/major-version)
[_navigate_before_ Why Go](https://go.dev/doc/modules/major-version)
    * [ Case Studies ](https://go.dev/solutions/case-studies)
    * [ Use Cases ](https://go.dev/solutions/use-cases)
    * [ Security ](https://go.dev/security/)
  * [Learn](https://go.dev/learn/)
  * [Docs _navigate_next_](https://go.dev/doc/modules/major-version)
[_navigate_before_ Docs](https://go.dev/doc/modules/major-version)
    * [ Go Spec ](https://go.dev/ref/spec)
    * [ Go User Manual ](https://go.dev/doc)
    * [ Standard library ](https://pkg.go.dev/std)
    * [ Release Notes ](https://go.dev/doc/devel/release)
    * [ Effective Go ](https://go.dev/doc/effective_go)
  * [Packages](https://pkg.go.dev)
  * [Community _navigate_next_](https://go.dev/doc/modules/major-version)
[_navigate_before_ Community](https://go.dev/doc/modules/major-version)
    * [ Recorded Talks ](https://go.dev/talks/)
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
    * [ Go blog ](https://go.dev/blog)
    * [ Go project ](https://go.dev/help)
    * Get connected


# Developing a major version update
Table of Contents
---

[Considerations for a major version update](https://go.dev/doc/modules/major-version#considerations)


[Branching for a major release](https://go.dev/doc/modules/major-version#branching)
|
You must update to a major version when changes you’re making in a potential new version can’t guarantee backward compatibility for the module’s users. For example, you’ll make this change if you change your module’s public API such that it breaks client code using previous versions of the module.
> **Note:** Each release type – major, minor, patch, or pre-release – has a different meaning for a module’s users. Those users rely on these differences to understand the level of risk a release represents to their own code. In other words, when preparing a release, be sure that its version number accurately reflects the nature of the changes since the preceding release. For more on version numbers, see [Module version numbering](https://go.dev/doc/modules/version-numbers).
**See also**
  * For an overview of module development, see [Developing and publishing modules](https://go.dev/doc/modules/developing).
  * For an end-to-end view, see [Module release and versioning workflow](https://go.dev/doc/modules/release-workflow).


## Considerations for a major version update[¶](https://go.dev/doc/modules/major-version#considerations)
You should only update to a new major version when it’s absolutely necessary. A major version update represents significant churn for both you and your module’s users. When you’re considering a major version update, think about the following:
  * Be clear with your users about what releasing the new major version means for your support of previous major versions.
Are previous versions deprecated? Supported as they were before? Will you be maintaining previous versions, including with bug fixes?
  * Be ready to take on the maintenance of two versions: the old and the new. For example, if you fix bugs in one, you’ll often be porting those fixes into the other.
  * Remember that a new major version is a new module from a dependency management perspective. Your users will need to update to use a new module after you release, rather than simply upgrading.
That’s because a new major version has a different module path from the preceding major version. For example, for a module whose module path is example.com/mymodule, a v2 version would have the module path example.com/mymodule/v2.
  * When you’re developing a new major version, you must also update import paths wherever code imports packages from the new module. Your module’s users must also update their import paths if they want to upgrade to the new major version.


## Branching for a major release[¶](https://go.dev/doc/modules/major-version#branching)
The most straightforward approach to handling source when preparing to develop a new major version is to branch the repository at the latest version of the previous major version.
For example, in a command prompt you might change to your module’s root directory, then create a new v2 branch there.
```
$ cd mymodule
$ git checkout -b v2
Switched to a new branch "v2"

```

![Diagram illustrating a repository branched from master to v2](https://go.dev/doc/modules/images/v2-branch-module.png)
Once you have the source branched, you’ll need to make the following changes to the source for your new version:
  * In the new version’s go.mod file, append new major version number to the module path, as in the following example:
    * Existing version: `example.com/mymodule`
    * New version: `example.com/mymodule/v2`
  * In your Go code, update every imported package path where you import a package from the module, appending the major version number to the module path portion.
    * Old import statement: `import "example.com/mymodule/package1"`
    * New import statement: `import "example.com/mymodule/v2/package1"`


For publishing steps, see [Publishing a module](https://go.dev/doc/modules/publishing).
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
