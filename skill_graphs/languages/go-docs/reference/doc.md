[ ![Go](https://go.dev/images/go-logo-white.svg) ](https://go.dev/)
[ Skip to Main Content ](https://go.dev/doc/#main-content)
  * [ Why Go _arrow_drop_down_ ](https://go.dev/doc/)
Press Enter to activate/deactivate dropdown
    * [ Case Studies ](https://go.dev/solutions/case-studies)
Common problems companies solve with Go
    * [ Use Cases ](https://go.dev/solutions/use-cases)
Stories about how and why companies use Go
    * [ Security ](https://go.dev/security/)
How Go can help keep you secure by default
  * [ Learn ](https://go.dev/learn/)
Press Enter to activate/deactivate dropdown
  * [ Docs _arrow_drop_down_ ](https://go.dev/doc/)
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
  * [ Community _arrow_drop_down_ ](https://go.dev/doc/)
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
  * [Why Go _navigate_next_](https://go.dev/doc/)
[_navigate_before_ Why Go](https://go.dev/doc/)
    * [ Case Studies ](https://go.dev/solutions/case-studies)
    * [ Use Cases ](https://go.dev/solutions/use-cases)
    * [ Security ](https://go.dev/security/)
  * [Learn](https://go.dev/learn/)
  * [Docs _navigate_next_](https://go.dev/doc/)
[_navigate_before_ Docs](https://go.dev/doc/)
    * [ Go Spec ](https://go.dev/ref/spec)
    * [ Go User Manual ](https://go.dev/doc)
    * [ Standard library ](https://pkg.go.dev/std)
    * [ Release Notes ](https://go.dev/doc/devel/release)
    * [ Effective Go ](https://go.dev/doc/effective_go)
  * [Packages](https://pkg.go.dev)
  * [Community _navigate_next_](https://go.dev/doc/)
[_navigate_before_ Community](https://go.dev/doc/)
    * [ Recorded Talks ](https://go.dev/talks/)
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
    * [ Go blog ](https://go.dev/blog)
    * [ Go project ](https://go.dev/help)
    * Get connected


# Documentation
The Go programming language is an open source project to make programmers more productive.
Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.
## Getting Started
###  [Installing Go](https://go.dev/doc/install)[¶](https://go.dev/doc/#installing)
Instructions for downloading and installing Go.
###  [Tutorial: Getting started](https://go.dev/doc/tutorial/getting-started.html)[¶](https://go.dev/doc/#get-started-tutorial)
A brief Hello, World tutorial to get started. Learn a bit about Go code, tools, packages, and modules.
###  [Tutorial: Create a module](https://go.dev/doc/tutorial/create-module.html)[¶](https://go.dev/doc/#create-module-tutorial)
A tutorial of short topics introducing functions, error handling, arrays, maps, unit testing, and compiling.
###  [Tutorial: Getting started with multi-module workspaces](https://go.dev/doc/tutorial/workspaces.html)[¶](https://go.dev/doc/#workspaces-tutorial)
Introduces the basics of creating and using multi-module workspaces in Go. Multi-module workspaces are useful for making changes across multiple modules.
###  [Tutorial: Developing a RESTful API with Go and Gin](https://go.dev/doc/tutorial/web-service-gin.html)[¶](https://go.dev/doc/#web-service-gin-tutorial)
Introduces the basics of writing a RESTful web service API with Go and the Gin Web Framework.
###  [Tutorial: Getting started with generics](https://go.dev/doc/tutorial/generics.html)[¶](https://go.dev/doc/#generics-tutorial)
With generics, you can declare and use functions or types that are written to work with any of a set of types provided by calling code.
###  [Tutorial: Getting started with fuzzing](https://go.dev/doc/tutorial/fuzz.html)[¶](https://go.dev/doc/#fuzz-tutorial)
Fuzzing can generate inputs to your tests that can catch edge cases and security issues that you may have missed.
###  [Writing Web Applications](https://go.dev/doc/articles/wiki/)[¶](https://go.dev/doc/#writing-web-applications)
Building a simple web application.
###  [How to write Go code](https://go.dev/doc/code.html)[¶](https://go.dev/doc/#code)
This doc explains how to develop a simple set of Go packages inside a module, and it shows how to use the [`go` command](https://go.dev/cmd/go/) to build and test packages.
###  [A Tour of Go](https://go.dev/tour/)[¶](https://go.dev/doc/#go_tour)
An interactive introduction to Go in four sections. The first section covers basic syntax and data structures; the second discusses methods and interfaces; the third is about Generics; and the fourth introduces Go's concurrency primitives. Each section concludes with a few exercises so you can practice what you've learned. You can [take the tour online](https://go.dev/tour/) or install it locally with:
```
	$ go install golang.org/x/website/tour@latest

	  ![](https://go.dev/images/icons/copy-paste.svg)
	  ![](https://go.dev/images/icons/copy-paste-dark.svg)


```

This will place the `tour` binary in your [GOPATH](https://go.dev/cmd/go/#hdr-GOPATH_and_Modules)'s `bin` directory.
## Using and understanding Go
###  [Effective Go](https://go.dev/doc/effective_go.html)[¶](https://go.dev/doc/#effective_go)
A document that gives tips for writing clear, idiomatic Go code. A must read for any new Go programmer. It augments the tour and the language specification, both of which should be read first.
###  [Frequently Asked Questions (FAQ)](https://go.dev/doc/faq)[¶](https://go.dev/doc/#faq)
Answers to common questions about Go.
###  [Editor plugins and IDEs](https://go.dev/doc/editors.html)[¶](https://go.dev/doc/#editors)
A document that summarizes commonly used editor plugins and IDEs with Go support.
###  [Diagnostics](https://go.dev/doc/diagnostics.html)[¶](https://go.dev/doc/#diagnostics)
Summarizes tools and methodologies to diagnose problems in Go programs.
###  [A Guide to the Go Garbage Collector](https://go.dev/doc/gc-guide)[¶](https://go.dev/doc/#gc-guide)
A document that describes how Go manages memory, and how to make the most of it.
###  [Managing dependencies](https://go.dev/doc/modules/managing-dependencies)[¶](https://go.dev/doc/#dependencies)
When your code uses external packages, those packages (distributed as modules) become dependencies.
###  [Fuzzing](https://go.dev/security/fuzz)[¶](https://go.dev/doc/#fuzzing)
Main documentation page for Go fuzzing.
###  [Coverage for Go applications](https://go.dev/doc/build-cover)[¶](https://go.dev/doc/#coverage)
Main documentation page for coverage testing of Go applications.
###  [Profile-guided optimization](https://go.dev/doc/pgo)[¶](https://go.dev/doc/#pgo)
Main documentation page for profile-guided optimization (PGO) of Go applications.
## References
###  [Package Documentation](https://go.dev/pkg/)[¶](https://go.dev/doc/#pkg)
The documentation for the Go standard library.
###  [Command Documentation](https://go.dev/doc/cmd)[¶](https://go.dev/doc/#cmd)
The documentation for the Go tools.
###  [Language Specification](https://go.dev/ref/spec)[¶](https://go.dev/doc/#spec)
The official Go Language specification.
###  [Go Modules Reference](https://go.dev/ref/mod)[¶](https://go.dev/doc/#mod)
A detailed reference manual for Go's dependency management system.
### [go.mod file reference](https://go.dev/doc/modules/gomod-ref)
Reference for the directives included in a go.mod file.
###  [The Go Memory Model](https://go.dev/ref/mem)[¶](https://go.dev/doc/#go_mem)
A document that specifies the conditions under which reads of a variable in one goroutine can be guaranteed to observe values produced by writes to the same variable in a different goroutine.
###  [Contribution Guide](https://go.dev/doc/contribute)[¶](https://go.dev/doc/#contributing)
Contributing to Go.
###  [Release History](https://go.dev/doc/devel/release.html)[¶](https://go.dev/doc/#release)
A summary of the changes between Go releases.
## Accessing databases
###  [Tutorial: Accessing a relational database](https://go.dev/doc/tutorial/database-access)[¶](https://go.dev/doc/#data-access-tutorial)
Introduces the basics of accessing a relational database using Go and the `database/sql` package in the standard library.
###  [Accessing relational databases](https://go.dev/doc/database/index)[¶](https://go.dev/doc/#accessing-databases)
An overview of Go's data access features.
###  [Opening a database handle](https://go.dev/doc/database/open-handle)[¶](https://go.dev/doc/#open-handle)
You use the Go database handle to execute database operations. Once you open a handle with database connection properties, the handle represents a connection pool it manages on your behalf.
###  [Executing SQL statements that don't return data](https://go.dev/doc/database/change-data)[¶](https://go.dev/doc/#change-data)
For SQL operations that might change the database, including SQL `INSERT`, `UPDATE`, and `DELETE`, you use `Exec` methods.
###  [Querying for data](https://go.dev/doc/database/querying)[¶](https://go.dev/doc/#querying)
For `SELECT` statements that return data from a query, using the `Query` or `QueryRow` method.
###  [Using prepared statements](https://go.dev/doc/database/prepared-statements)[¶](https://go.dev/doc/#prepared-statements)
Defining a prepared statement for repeated use can help your code run a bit faster by avoiding the overhead of re-creating the statement each time your code performs the database operation.
###  [Executing transactions](https://go.dev/doc/database/execute-transactions)[¶](https://go.dev/doc/#execute-transactions)
`sql.Tx` exports methods representing transaction-specific semantics, including `Commit` and `Rollback`, as well as methods you use to perform common database operations.
###  [Canceling in-progress database operations](https://go.dev/doc/database/cancel-operations)[¶](https://go.dev/doc/#cancel-operations)
Using [context.Context](https://pkg.go.dev/context#Context), you can have your application's function calls and services stop working early and return an error when their processing is no longer needed.
###  [Managing connections](https://go.dev/doc/database/manage-connections)[¶](https://go.dev/doc/#manage-connections)
For some advanced programs, you might need to tune connection pool parameters or work with connections explicitly.
###  [Avoiding SQL injection risk](https://go.dev/doc/database/sql-injection)[¶](https://go.dev/doc/#sql-injection)
You can avoid an SQL injection risk by providing SQL parameter values as `sql` package function arguments
## Developing modules
###  [Developing and publishing modules](https://go.dev/doc/modules/developing)[¶](https://go.dev/doc/#modules-develop-publish)
You can collect related packages into modules, then publish the modules for other developers to use. This topic gives an overview of developing and publishing modules.
###  [Module release and versioning workflow](https://go.dev/doc/modules/release-workflow)[¶](https://go.dev/doc/#modules-release-workflow)
When you develop modules for use by other developers, you can follow a workflow that helps ensure a reliable, consistent experience for developers using the module. This topic describes the high-level steps in that workflow.
###  [Managing module source](https://go.dev/doc/modules/managing-source)[¶](https://go.dev/doc/#modules-managing-source)
When you're developing modules to publish for others to use, you can help ensure that your modules are easier for other developers to use by following the repository conventions described in this topic.
###  [Organizing a Go module](https://go.dev/doc/modules/layout)[¶](https://go.dev/doc/#modules-layout)
What is the right way to organize the files and directories in a typical Go project? This topic discusses some common layouts depending on the kind of module you have.
###  [Developing a major version update](https://go.dev/doc/modules/major-version)[¶](https://go.dev/doc/#modules-major-version)
A major version update can be very disruptive to your module's users because it includes breaking changes and represents a new module. Learn more in this topic.
###  [Publishing a module](https://go.dev/doc/modules/publishing)[¶](https://go.dev/doc/#modules-publishing)
When you want to make a module available for other developers, you publish it so that it's visible to Go tools. Once you've published the module, developers importing its packages will be able to resolve a dependency on the module by running commands such as `go get`.
###  [Module version numbering](https://go.dev/doc/modules/version-numbers)[¶](https://go.dev/doc/#modules-version-numbers)
A module's developer uses each part of a module's version number to signal the version’s stability and backward compatibility. For each new release, a module's release version number specifically reflects the nature of the module's changes since the preceding release.
## Talks
### [¶](https://go.dev/doc/#video_tour_of_go)
Three things that make Go fast, fun, and productive: interfaces, reflection, and concurrency. Builds a toy web crawler to demonstrate these.
### [¶](https://go.dev/doc/#go_code_that_grows)
One of Go's key design goals is code adaptability; that it should be easy to take a simple design and build upon it in a clean and natural way. In this talk Andrew Gerrand describes a simple "chat roulette" server that matches pairs of incoming TCP connections, and then use Go's concurrency mechanisms, interfaces, and standard library to extend it with a web interface and other features. While the function of the program changes dramatically, Go's flexibility preserves the original design as it grows.
### [¶](https://go.dev/doc/#go_concurrency_patterns)
Concurrency is the key to designing high performance network services. Go's concurrency primitives (goroutines and channels) provide a simple and efficient means of expressing concurrent execution. In this talk we see how tricky concurrency problems can be solved gracefully with simple Go code.
### [¶](https://go.dev/doc/#advanced_go_concurrency_patterns)
This talk expands on the _Go Concurrency Patterns_ talk to dive deeper into Go's concurrency primitives.
#### More[¶](https://go.dev/doc/#talks_more)
See the [Go Talks site](https://go.dev/talks) and [wiki page](https://go.dev/wiki/GoTalks) for more Go talks.
## Codewalks
Guided tours of Go programs.
  * [First-Class Functions in Go](https://go.dev/doc/codewalk/functions)
  * [Generating arbitrary text: a Markov chain algorithm](https://go.dev/doc/codewalk/markov)
  * [Share Memory by Communicating](https://go.dev/doc/codewalk/sharemem)


### Language
  * [JSON-RPC: a tale of interfaces](https://go.dev/blog/json-rpc-tale-of-interfaces)
  * [Go's Declaration Syntax](https://go.dev/blog/gos-declaration-syntax)
  * [Defer, Panic, and Recover](https://go.dev/blog/defer-panic-and-recover)
  * [Go Concurrency Patterns: Timing out, moving on](https://go.dev/blog/go-concurrency-patterns-timing-out-and)
  * [Go Slices: usage and internals](https://go.dev/blog/go-slices-usage-and-internals)
  * [A GIF decoder: an exercise in Go interfaces](https://go.dev/blog/gif-decoder-exercise-in-go-interfaces)
  * [Error Handling and Go](https://go.dev/blog/error-handling-and-go)


### Packages
  * [JSON and Go](https://go.dev/blog/json-and-go) - using the [json](https://go.dev/pkg/encoding/json/) package.
  * [Gobs of data](https://go.dev/blog/gobs-of-data) - the design and use of the [gob](https://go.dev/pkg/encoding/gob/) package.
  * [The Laws of Reflection](https://go.dev/blog/laws-of-reflection) - the fundamentals of the [reflect](https://go.dev/pkg/reflect/) package.
  * [The Go image package](https://go.dev/blog/go-image-package) - the fundamentals of the [image](https://go.dev/pkg/image/) package.
  * [The Go image/draw package](https://go.dev/blog/go-imagedraw-package) - the fundamentals of the [image/draw](https://go.dev/pkg/image/draw/) package.


### Modules
  * [Using Go Modules](https://go.dev/blog/using-go-modules) - an introduction to using modules in a simple project.
  * [Migrating to Go Modules](https://go.dev/blog/migrating-to-go-modules) - converting an existing project to use modules.
  * [Publishing Go Modules](https://go.dev/blog/publishing-go-modules) - how to make new versions of modules available to others.
  * [Go Modules: v2 and Beyond](https://go.dev/blog/v2-go-modules) - creating and publishing major versions 2 and higher.
  * [Keeping Your Modules Compatible](https://go.dev/blog/module-compatibility) - how to keep your modules compatible with prior minor/patch versions.


### Tools
  * [About the Go command](https://go.dev/doc/articles/go_command.html) - why we wrote it, what it is, what it's not, and how to use it.
  * [Go Doc Comments](https://go.dev/doc/comment) - writing good program documentation
  * [Debugging Go Code with GDB](https://go.dev/doc/gdb)
  * [Data Race Detector](https://go.dev/doc/articles/race_detector.html) - a manual for the data race detector.
  * [A Quick Guide to Go's Assembler](https://go.dev/doc/asm) - an introduction to the assembler used by Go.
  * [C? Go? Cgo!](https://go.dev/blog/c-go-cgo) - linking against C code with [cgo](https://go.dev/cmd/cgo/).
  * [Profiling Go Programs](https://go.dev/blog/profiling-go-programs) - tools for measuring your code's CPU and memory usage
  * [Introducing the Go Race Detector](https://go.dev/blog/race-detector) - an introduction to the race detector.
  * [Gopls: The language server for Go ](https://go.dev/gopls) - getting the most out your editor when working in Go.


## Wiki
The [Go Wiki](https://go.dev/wiki), maintained by the Go community, includes articles about the Go language, tools, and other resources.
See the [Learn](https://go.dev/wiki/Learn) page at the [Wiki](https://go.dev/wiki) for more Go learning resources.
## Non-English Documentation
See the [NonEnglish](https://go.dev/wiki/NonEnglish) page at the [Wiki](https://go.dev/wiki) for localized documentation.
Opens in new window.
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
