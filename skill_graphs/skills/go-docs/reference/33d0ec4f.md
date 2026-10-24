## Writing Code[¶](https://go.dev/doc/faq#Writing_Code)
### How are libraries documented?[¶](https://go.dev/doc/faq#How_are_libraries_documented)
For access to documentation from the command line, the [go](https://go.dev/pkg/cmd/go/) tool has a [doc](https://go.dev/pkg/cmd/go/#hdr-Show_documentation_for_package_or_symbol) subcommand that provides a textual interface to the documentation for declarations, files, packages and so on.
The global package discovery page [pkg.go.dev/pkg/](https://go.dev/pkg/). runs a server that extracts package documentation from Go source code anywhere on the web and serves it as HTML with links to the declarations and related elements. It is the easiest way to learn about existing Go libraries.
In the early days of the project, there was a similar program, `godoc`, that could also be run to extract documentation for files on the local machine; [pkg.go.dev/pkg/](https://go.dev/pkg/) is essentially a descendant. Another descendant is the [`pkgsite`](https://pkg.go.dev/golang.org/x/pkgsite/cmd/pkgsite) command that, like `godoc`, can be run locally, although it is not yet integrated into the results shown by `go` `doc`.
### Is there a Go programming style guide?[¶](https://go.dev/doc/faq#Is_there_a_Go_programming_style_guide)
There is no explicit style guide, although there is certainly a recognizable “Go style”.
Go has established conventions to guide decisions around naming, layout, and file organization. The document [Effective Go](https://go.dev/doc/effective_go.html) contains some advice on these topics. More directly, the program `gofmt` is a pretty-printer whose purpose is to enforce layout rules; it replaces the usual compendium of dos and don’ts that allows interpretation. All the Go code in the repository, and the vast majority in the open source world, has been run through `gofmt`.
The document titled [Go Code Review Comments](https://go.dev/s/comments) is a collection of very short essays about details of Go idiom that are often missed by programmers. It is a handy reference for people doing code reviews for Go projects.
### How do I submit patches to the Go libraries?[¶](https://go.dev/doc/faq#How_do_I_submit_patches_to_the_Go_libraries)
The library sources are in the `src` directory of the repository. If you want to make a significant change, please discuss on the mailing list before embarking.
See the document [Contributing to the Go project](https://go.dev/doc/contribute.html) for more information about how to proceed.
### Why does “go get” use HTTPS when cloning a repository?[¶](https://go.dev/doc/faq#git_https)
Companies often permit outgoing traffic only on the standard TCP ports 80 (HTTP) and 443 (HTTPS), blocking outgoing traffic on other ports, including TCP port 9418 (git) and TCP port 22 (SSH). When using HTTPS instead of HTTP, `git` enforces certificate validation by default, providing protection against man-in-the-middle, eavesdropping and tampering attacks. The `go get` command therefore uses HTTPS for safety.
`Git` can be configured to authenticate over HTTPS or to use SSH in place of HTTPS. To authenticate over HTTPS, you can add a line to the `$HOME/.netrc` file that git consults:
```
machine github.com login *USERNAME* password *APIKEY*

```

For GitHub accounts, the password can be a
`Git` can also be configured to use SSH in place of HTTPS for URLs matching a given prefix. For example, to use SSH for all GitHub access, add these lines to your `~/.gitconfig`:
```
[url "ssh://git@github.com/"]
    insteadOf = https://github.com/

```

When working with private modules, but using a public module proxy for dependencies, you may need to set `GOPRIVATE`. See [private modules](https://go.dev/ref/mod#private-modules) for details and additional settings.
### How should I manage package versions using “go get”?[¶](https://go.dev/doc/faq#get_version)
The Go toolchain has a built-in system for managing versioned sets of related packages, known as _modules_. Modules were introduced in [Go 1.11](https://go.dev/doc/go1.11#modules) and have been ready for production use since [1.14](https://go.dev/doc/go1.14#introduction).
To create a project using modules, run [`go mod init`](https://go.dev/ref/mod#go-mod-init). This command creates a `go.mod` file that tracks dependency versions.
```
go mod init example/project

```

To add, upgrade, or downgrade a dependency, run [`go get`](https://go.dev/ref/mod#go-get):
```
go get golang.org/x/text@v0.3.5

```

See [Tutorial: Create a module](https://go.dev/doc/tutorial/create-module.html) for more information on getting started.
See [Developing modules](https://go.dev/doc/#developing-modules) for guides on managing dependencies with modules.
Packages within modules should maintain backward compatibility as they evolve, following the
> If an old package and a new package have the same import path,
>  the new package must be backwards compatible with the old package.
The [Go 1 compatibility guidelines](https://go.dev/doc/go1compat.html) are a good reference here: don’t remove exported names, encourage tagged composite literals, and so on. If different functionality is required, add a new name instead of changing an old one.
Modules codify this with [major version suffix](https://go.dev/ref/mod#major-version-suffixes) as part of their path (like `/v2`). This preserves the import compatibility rule: packages in different major versions of a module have distinct paths.
