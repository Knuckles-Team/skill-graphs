[ ![Go](https://go.dev/images/go-logo-white.svg) ](https://go.dev/)
[ Skip to Main Content ](https://go.dev/doc/modules/version-numbers#main-content)
  * [ Why Go _arrow_drop_down_ ](https://go.dev/doc/modules/version-numbers)
Press Enter to activate/deactivate dropdown
    * [ Case Studies ](https://go.dev/solutions/case-studies)
Common problems companies solve with Go
    * [ Use Cases ](https://go.dev/solutions/use-cases)
Stories about how and why companies use Go
    * [ Security ](https://go.dev/security/)
How Go can help keep you secure by default
  * [ Learn ](https://go.dev/learn/)
Press Enter to activate/deactivate dropdown
  * [ Docs _arrow_drop_down_ ](https://go.dev/doc/modules/version-numbers)
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
  * [ Community _arrow_drop_down_ ](https://go.dev/doc/modules/version-numbers)
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
  * [Why Go _navigate_next_](https://go.dev/doc/modules/version-numbers)
[_navigate_before_ Why Go](https://go.dev/doc/modules/version-numbers)
    * [ Case Studies ](https://go.dev/solutions/case-studies)
    * [ Use Cases ](https://go.dev/solutions/use-cases)
    * [ Security ](https://go.dev/security/)
  * [Learn](https://go.dev/learn/)
  * [Docs _navigate_next_](https://go.dev/doc/modules/version-numbers)
[_navigate_before_ Docs](https://go.dev/doc/modules/version-numbers)
    * [ Go Spec ](https://go.dev/ref/spec)
    * [ Go User Manual ](https://go.dev/doc)
    * [ Standard library ](https://pkg.go.dev/std)
    * [ Release Notes ](https://go.dev/doc/devel/release)
    * [ Effective Go ](https://go.dev/doc/effective_go)
  * [Packages](https://pkg.go.dev)
  * [Community _navigate_next_](https://go.dev/doc/modules/version-numbers)
[_navigate_before_ Community](https://go.dev/doc/modules/version-numbers)
    * [ Recorded Talks ](https://go.dev/talks/)
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
    * [ Go blog ](https://go.dev/blog)
    * [ Go project ](https://go.dev/help)
    * Get connected


# Module version numbering
Table of Contents
---

[In development](https://go.dev/doc/modules/version-numbers#in-development)
    [Pseudo-version number](https://go.dev/doc/modules/version-numbers#pseudo-version-number)     [v0 number](https://go.dev/doc/modules/version-numbers#v0-number)

[Pre-release version](https://go.dev/doc/modules/version-numbers#pre-release-version)


[Minor version](https://go.dev/doc/modules/version-numbers#minor-version)


[Patch version](https://go.dev/doc/modules/version-numbers#patch-version)


[Major version](https://go.dev/doc/modules/version-numbers#major-version)
|
A module’s developer uses each part of a module’s version number to signal the version’s stability and backward compatibility. For each new release, a module’s release version number specifically reflects the nature of the module’s changes since the preceding release.
When you’re developing code that uses external modules, you can use the version numbers to understand an external module’s stability when you’re considering an upgrade. When you’re developing your own modules, your version numbers will signal your modules’ stability and backward compatibility to other developers.
This topic describes what module version numbers mean.
**See also**
  * When you’re using external packages in your code, you can manage those dependencies with Go tools. For more, see [Managing dependencies](https://go.dev/doc/modules/managing-dependencies).
  * If you’re developing modules for others to use, you apply a version number when you publish the module, tagging the module in its repository. For more, see [Publishing a module](https://go.dev/doc/modules/publishing).


A released module is published with a version number in the semantic versioning model, as in the following illustration:
![Diagram illustrating a semantic version number showing major version 1, minor version 4, patch version 0, and pre-release version beta 2](https://go.dev/doc/modules/images/version-number.png)
The following table describes how the parts of a version number signify a module’s stability and backward compatibility.
Version stage | Example | Message to developers
---|---|---
[In development](https://go.dev/doc/modules/version-numbers#in-development) | Automatic pseudo-version number v**0**.x.x | Signals that the module is still **in development and unstable**. This release carries no backward compatibility or stability guarantees.
[Major version](https://go.dev/doc/modules/version-numbers#major) | v**1**.x.x | Signals **backward-incompatible public API changes**. This release carries no guarantee that it will be backward compatible with preceding major versions.
[Minor version](https://go.dev/doc/modules/version-numbers#minor) | vx.**4**.x | Signals **backward-compatible public API changes**. This release guarantees backward compatibility and stability.
[Patch version](https://go.dev/doc/modules/version-numbers#patch) | vx.x.**1** | Signals **changes that don't affect the module's public API** or its dependencies. This release guarantees backward compatibility and stability.
[Pre-release version](https://go.dev/doc/modules/version-numbers#pre-release) | vx.x.x-**beta.2** | Signals that this is a **pre-release milestone, such as an alpha or beta**. This release carries no stability guarantees.
## In development[¶](https://go.dev/doc/modules/version-numbers#in-development)
Signals that the module is still in development and **unstable**. This release carries no backward compatibility or stability guarantees.
The version number can take one of the following forms:
**Pseudo-version number**
> v0.0.0-20170915032832-14c0d48ead0c
**v0 number**
> v0.x.x
### Pseudo-version number[¶](https://go.dev/doc/modules/version-numbers#pseudo-version-number)
When a module has not been tagged in its repository, Go tools will generate a pseudo-version number for use in the go.mod file of code that calls functions in the module.
**Note:** As a best practice, always allow Go tools to generate the pseudo-version number rather than creating your own.
Pseudo-versions are useful when a developer of code consuming the module’s functions needs to develop against a commit that hasn’t been tagged with a semantic version tag yet.
A pseudo-version number has three parts separated by dashes, as shown in the following form:
#### Syntax[¶](https://go.dev/doc/modules/version-numbers#syntax)
_baseVersionPrefix_ -_timestamp_ -_revisionIdentifier_
#### Parts[¶](https://go.dev/doc/modules/version-numbers#parts)
  * **baseVersionPrefix** (vX.0.0 or vX.Y.Z-0) is a value derived either from a semantic version tag that precedes the revision or from vX.0.0 if there is no such tag.
  * **timestamp** (yymmddhhmmss) is the UTC time the revision was created. In Git, this is the commit time, not the author time.
  * **revisionIdentifier** (abcdefabcdef) is a 12-character prefix of the commit hash, or in Subversion, a zero-padded revision number.


### v0 number[¶](https://go.dev/doc/modules/version-numbers#v0-number)
A module published with a v0 number will have a formal semantic version number with a major, minor, and patch part, as well as an optional pre-release identifier.
Though a v0 version can be used in production, it makes no stability or backward compatibility guarantees. In addition, versions v1 and later are allowed to break backward compatibility for code using the v0 versions. For this reason, a developer with code consuming functions in a v0 module is responsible for adapting to incompatible changes until v1 is released.
## Pre-release version[¶](https://go.dev/doc/modules/version-numbers#pre-release-version)
Signals that this is a pre-release milestone, such as an alpha or beta. This release carries no stability guarantees.
#### Example[¶](https://go.dev/doc/modules/version-numbers#example)
```
vx.x.x-beta.2

```

A module’s developer can use a pre-release identifier with any major.minor.patch combination by appending a hyphen and the pre-release identifier.
## Minor version[¶](https://go.dev/doc/modules/version-numbers#minor-version)
Signals backward-compatible changes to the module’s public API. This release guarantees backward compatibility and stability.
#### Example[¶](https://go.dev/doc/modules/version-numbers#example-1)
```
vx.4.x

```

This version changes the module’s public API, but not in a way that breaks calling code. This might include changes to a module’s own dependencies or the addition of new functions, methods, struct fields, or types.
In other words, this version might include enhancements through new functions that another developer might want to use. However, a developer using previous minor versions needn’t change their code otherwise.
## Patch version[¶](https://go.dev/doc/modules/version-numbers#patch-version)
Signals changes that don’t affect the module’s public API or its dependencies. This release guarantees backward compatibility and stability.
#### Example[¶](https://go.dev/doc/modules/version-numbers#example-2)
```
vx.x.1

```

An update that increments this number is only for minor changes such as bug fixes. Developers of consuming code can upgrade to this version safely without needing to change their code.
## Major version[¶](https://go.dev/doc/modules/version-numbers#major-version)
Signals backward-incompatible changes in a module’s public API. This release carries no guarantee that it will be backward compatible with preceding major versions.
#### Example[¶](https://go.dev/doc/modules/version-numbers#example-3)
v1.x.x
A v1 or above version number signals that the module is stable for use (with exceptions for its pre-release versions).
Note that because a version 0 makes no stability or backward compatibility guarantees, a developer upgrading a module from v0 to v1 is responsible for adapting to changes that break backward compatibility.
A module developer should increment this number past v1 only when necessary because the version upgrade represents significant disruption for developers whose code uses function in the upgraded module. This disruption includes backward-incompatible changes to the public API, as well as the need for developers using the module to update the package path wherever they import packages from the module.
A major version update to a number higher than v1 will also have a new module path. That’s because the module path will have the major version number appended, as in the following example:
```
module example.com/mymodule/v2 v2.0.0

```

A major version update makes this a new module with a separate history from the module’s previous version. If you’re developing modules to publish for others, see “Publishing breaking API changes” in [Module release and versioning workflow](https://go.dev/doc/modules/release-workflow).
For more on the module directive, see [go.mod reference](https://go.dev/doc/modules/gomod-ref).
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
