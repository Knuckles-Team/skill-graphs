# A Guide to the Go Garbage Collector
Table of Contents
---

[Introduction](https://go.dev/doc/gc-guide#Introduction)
    [Where Go Values Live](https://go.dev/doc/gc-guide#Where_Go_Values_Live)     [Tracing Garbage Collection](https://go.dev/doc/gc-guide#Tracing_Garbage_Collection)

[The GC cycle](https://go.dev/doc/gc-guide#The_GC_cycle)
    [Understanding costs](https://go.dev/doc/gc-guide#Understanding_costs)     [GOGC](https://go.dev/doc/gc-guide#GOGC)     [Memory limit](https://go.dev/doc/gc-guide#Memory_limit)     [Latency](https://go.dev/doc/gc-guide#Latency)     [Finalizers, cleanups, and weak pointers](https://go.dev/doc/gc-guide#Finalizers_cleanups_and_weak_pointers)     [Additional resources](https://go.dev/doc/gc-guide#Additional_resources) |

[A note about virtual memory](https://go.dev/doc/gc-guide#A_note_about_virtual_memory)


[Optimization guide](https://go.dev/doc/gc-guide#Optimization_guide)
    [Identifying costs](https://go.dev/doc/gc-guide#Identifying_costs)     [Eliminating heap allocations](https://go.dev/doc/gc-guide#Eliminating_heap_allocations)     [Implementation-specific optimizations](https://go.dev/doc/gc-guide#Implementation-specific_optimizations)     [Linux transparent huge pages (THP)](https://go.dev/doc/gc-guide#Linux_transparent_huge_pages)

[Appendix](https://go.dev/doc/gc-guide#Appendix)
    [Additional notes on GOGC](https://go.dev/doc/gc-guide#Additional_notes_on_GOGC)
