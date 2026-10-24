[ ![Go](https://go.dev/images/go-logo-white.svg) ](https://go.dev/)
[ Skip to Main Content ](https://go.dev/doc/modules/publishing#main-content)
  * [ Why Go _arrow_drop_down_ ](https://go.dev/doc/modules/publishing)
Press Enter to activate/deactivate dropdown
    * [ Case Studies ](https://go.dev/solutions/case-studies)
Common problems companies solve with Go
    * [ Use Cases ](https://go.dev/solutions/use-cases)
Stories about how and why companies use Go
    * [ Security ](https://go.dev/security/)
How Go can help keep you secure by default
  * [ Learn ](https://go.dev/learn/)
Press Enter to activate/deactivate dropdown
  * [ Docs _arrow_drop_down_ ](https://go.dev/doc/modules/publishing)
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
  * [ Community _arrow_drop_down_ ](https://go.dev/doc/modules/publishing)
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
  * [Why Go _navigate_next_](https://go.dev/doc/modules/publishing)
[_navigate_before_ Why Go](https://go.dev/doc/modules/publishing)
    * [ Case Studies ](https://go.dev/solutions/case-studies)
    * [ Use Cases ](https://go.dev/solutions/use-cases)
    * [ Security ](https://go.dev/security/)
  * [Learn](https://go.dev/learn/)
  * [Docs _navigate_next_](https://go.dev/doc/modules/publishing)
[_navigate_before_ Docs](https://go.dev/doc/modules/publishing)
    * [ Go Spec ](https://go.dev/ref/spec)
    * [ Go User Manual ](https://go.dev/doc)
    * [ Standard library ](https://pkg.go.dev/std)
    * [ Release Notes ](https://go.dev/doc/devel/release)
    * [ Effective Go ](https://go.dev/doc/effective_go)
  * [Packages](https://pkg.go.dev)
  * [Community _navigate_next_](https://go.dev/doc/modules/publishing)
[_navigate_before_ Community](https://go.dev/doc/modules/publishing)
    * [ Recorded Talks ](https://go.dev/talks/)
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
    * [ Go blog ](https://go.dev/blog)
    * [ Go project ](https://go.dev/help)
    * Get connected


# Publishing a module
When you want to make a module available for other developers, you publish it so that it’s visible to Go tools. Once you’ve published the module, developers importing its packages will be able to resolve a dependency on the module by running commands such as `go get`.
> **Note:** Don’t change a tagged version of a module after publishing it. For developers using the module, Go tools authenticate a downloaded module against the first downloaded copy. If the two differ, Go tools will return a security error. Instead of changing the code for a previously published version, publish a new version.
**See also**
  * For an overview of module development, see [Developing and publishing modules](https://go.dev/doc/modules/developing)
  * For a high-level module development workflow – which includes publishing – see [Module release and versioning workflow](https://go.dev/doc/modules/release-workflow).


## Publishing steps[¶](https://go.dev/doc/modules/publishing#publishing-steps)
Use the following steps to publish a module.
  1. Open a command prompt and change to your module’s root directory in the local repository.
  2. Run `go mod tidy`, which removes any dependencies the module might have accumulated that are no longer necessary.
```
$ go mod tidy

```

  3. Run `go test ./...` a final time to make sure everything is working.
This runs the unit tests you’ve written to use the Go testing framework.
```
$ go test ./...
ok      example.com/mymodule       0.015s

```

  4. Tag the project with a new version number using the `git tag` command.
For the version number, use a number that signals to users the nature of changes in this release. For more, see [Module version numbering](https://go.dev/doc/modules/version-numbers).
```
$ git commit -m "mymodule: changes for v0.1.0"
$ git tag v0.1.0

```

  5. Push the new tag to the origin repository.
```
$ git push origin v0.1.0

```

  6. Make the module available by running the [`go list` command](https://go.dev/cmd/go/#hdr-List_packages_or_modules) to prompt Go to update its index of modules with information about the module you’re publishing.
Precede the command with a statement to set the `GOPROXY` environment variable to a Go proxy. This will ensure that your request reaches the proxy.
```
$ GOPROXY=proxy.golang.org go list -m example.com/mymodule@v0.1.0

```



Developers interested in your module import a package from it and run the [`go get` command](https://go.dev/doc/modules/publishing) just as they would with any other module. They can run the [`go get` command](https://go.dev/doc/modules/publishing) for latest versions or they can specify a particular version, as in the following example:
```
$ go get example.com/mymodule@v0.1.0

```

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
