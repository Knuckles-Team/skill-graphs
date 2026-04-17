## Performance[¶](https://go.dev/doc/faq#Performance)
### Why does Go perform badly on benchmark X?[¶](https://go.dev/doc/faq#Why_does_Go_perform_badly_on_benchmark_x)
One of Go’s design goals is to approach the performance of C for comparable programs, yet on some benchmarks it does quite poorly, including several in [regexp package](https://go.dev/pkg/regexp) to mature, highly optimized regular expression libraries like PCRE.
Benchmark games are won by extensive tuning and the Go versions of most of the benchmarks need attention. If you measure truly comparable C and Go programs (
Still, there is room for improvement. The compilers are good but could be better, many libraries need major performance work, and the garbage collector isn’t fast enough yet. (Even if it were, taking care not to generate unnecessary garbage can have a huge effect.)
In any case, Go can often be very competitive. There has been significant improvement in the performance of many programs as the language and tools have developed. See the blog post about [profiling Go programs](https://go.dev/blog/profiling-go-programs) for an informative example. It’s quite old but still contains helpful information.
