## Changes from C[¶](https://go.dev/doc/faq#change_from_c)
### Why is the syntax so different from C?[¶](https://go.dev/doc/faq#different_syntax)
Other than declaration syntax, the differences are not major and stem from two desires. First, the syntax should feel light, without too many mandatory keywords, repetition, or arcana. Second, the language has been designed to be easy to analyze and can be parsed without a symbol table. This makes it much easier to build tools such as debuggers, dependency analyzers, automated documentation extractors, IDE plug-ins, and so on. C and its descendants are notoriously difficult in this regard.
### Why are declarations backwards?[¶](https://go.dev/doc/faq#declarations_backwards)
They’re only backwards if you’re used to C. In C, the notion is that a variable is declared like an expression denoting its type, which is a nice idea, but the type and expression grammars don’t mix very well and the results can be confusing; consider function pointers. Go mostly separates expression and type syntax and that simplifies things (using prefix `*` for pointers is an exception that proves the rule). In C, the declaration
```
    int* a, b;

```

declares `a` to be a pointer but not `b`; in Go
```
    var a, b *int

```

declares both to be pointers. This is clearer and more regular. Also, the `:=` short declaration form argues that a full variable declaration should present the same order as `:=` so
```
    var a uint64 = 1

```

has the same effect as
```
    a := uint64(1)

```

Parsing is also simplified by having a distinct grammar for types that is not just the expression grammar; keywords such as `func` and `chan` keep things clear.
See the article about [Go’s Declaration Syntax](https://go.dev/doc/articles/gos_declaration_syntax.html) for more details.
### Why is there no pointer arithmetic?[¶](https://go.dev/doc/faq#no_pointer_arithmetic)
Safety. Without pointer arithmetic it’s possible to create a language that can never derive an illegal address that succeeds incorrectly. Compiler and hardware technology have advanced to the point where a loop using array indices can be as efficient as a loop using pointer arithmetic. Also, the lack of pointer arithmetic can simplify the implementation of the garbage collector.
### Why are `++` and `--` statements and not expressions? And why postfix, not prefix?[¶](https://go.dev/doc/faq#inc_dec)
Without pointer arithmetic, the convenience value of pre- and postfix increment operators drops. By removing them from the expression hierarchy altogether, expression syntax is simplified and the messy issues around order of evaluation of `++` and `--` (consider `f(i++)` and `p[i] = q[++i]`) are eliminated as well. The simplification is significant. As for postfix vs. prefix, either would work fine but the postfix version is more traditional; insistence on prefix arose with the STL, a library for a language whose name contains, ironically, a postfix increment.
### Why are there braces but no semicolons? And why can’t I put the opening brace on the next line? [¶](https://go.dev/doc/faq#semicolons)
Go uses brace brackets for statement grouping, a syntax familiar to programmers who have worked with any language in the C family. Semicolons, however, are for parsers, not for people, and we wanted to eliminate them as much as possible. To achieve this goal, Go borrows a trick from BCPL: the semicolons that separate statements are in the formal grammar but are injected automatically, without lookahead, by the lexer at the end of any line that could be the end of a statement. This works very well in practice but has the effect that it forces a brace style. For instance, the opening brace of a function cannot appear on a line by itself.
Some have argued that the lexer should do lookahead to permit the brace to live on the next line. We disagree. Since Go code is meant to be formatted automatically by [`gofmt`](https://go.dev/cmd/gofmt/), _some_ style must be chosen. That style may differ from what you’ve used in C or Java, but Go is a different language and `gofmt`’s style is as good as any other. More important—much more important—the advantages of a single, programmatically mandated format for all Go programs greatly outweigh any perceived disadvantages of the particular style. Note too that Go’s style means that an interactive implementation of Go can use the standard syntax one line at a time without special rules.
### Why do garbage collection? Won’t it be too expensive?[¶](https://go.dev/doc/faq#garbage_collection)
One of the biggest sources of bookkeeping in systems programs is managing the lifetimes of allocated objects. In languages such as C in which it is done manually, it can consume a significant amount of programmer time and is often the cause of pernicious bugs. Even in languages like C++ or Rust that provide mechanisms to assist, those mechanisms can have a significant effect on the design of the software, often adding programming overhead of its own. We felt it was critical to eliminate such programmer overheads, and advances in garbage collection technology in the last few years gave us confidence that it could be implemented cheaply enough, and with low enough latency, that it could be a viable approach for networked systems.
Much of the difficulty of concurrent programming has its roots in the object lifetime problem: as objects get passed among threads it becomes cumbersome to guarantee they become freed safely. Automatic garbage collection makes concurrent code far easier to write. Of course, implementing garbage collection in a concurrent environment is itself a challenge, but meeting it once rather than in every program helps everyone.
Finally, concurrency aside, garbage collection makes interfaces simpler because they don’t need to specify how memory is managed across them.
This is not to say that the recent work in languages like Rust that bring new ideas to the problem of managing resources is misguided; we encourage this work and are excited to see how it evolves. But Go takes a more traditional approach by addressing object lifetimes through garbage collection, and garbage collection alone.
The current implementation is a mark-and-sweep collector. If the machine is a multiprocessor, the collector runs on a separate CPU core in parallel with the main program. Major work on the collector in recent years has reduced pause times often to the sub-millisecond range, even for large heaps, all but eliminating one of the major objections to garbage collection in networked servers. Work continues to refine the algorithm, reduce overhead and latency further, and to explore new approaches. The 2018 [ISMM keynote](https://go.dev/blog/ismmkeynote) by Rick Hudson of the Go team describes the progress so far and suggests some future approaches.
On the topic of performance, keep in mind that Go gives the programmer considerable control over memory layout and allocation, much more than is typical in garbage-collected languages. A careful programmer can reduce the garbage collection overhead dramatically by using the language well; see the article about [profiling Go programs](https://go.dev/blog/profiling-go-programs) for a worked example, including a demonstration of Go’s profiling tools.
#### Release Notes
Learn about what's new in each Go release.
[View release notes](https://go.dev/doc/devel/release)
#### Code of Conduct
Guidelines for participating in Go community spaces and reporting process for handing issues.
[View more](https://go.dev/conduct)
#### Brand Guidelines
Guidance about reusing the Go logo, gopher mascot, etc.
[View guidelines](https://go.dev/blog/go-brand)
#### Contribute Guide
Learn how to file bugs, pull requests, or otherwise contribute to the Go ecosystem.
[View guide](https://go.dev/doc/contribute)
#### Get connected
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
