## Appendix[¶](https://go.dev/doc/gc-guide#Appendix)
### Additional notes on GOGC[¶](https://go.dev/doc/gc-guide#Additional_notes_on_GOGC)
The [GOGC section](https://go.dev/doc/gc-guide#GOGC) claimed that doubling GOGC doubles heap memory overheads and halves GC CPU costs. To see why, let's break it down mathematically.
Firstly, the heap target sets a target for the total heap size. This target, however, mainly influences the new heap memory, because the live heap is fundamental to the application.
_Target heap memory = Live heap + (Live heap + GC roots) * GOGC / 100_
_Total heap memory = Live heap + New heap memory_
_⇒_
_New heap memory = (Live heap + GC roots) * GOGC / 100_
From this we can see that doubling GOGC would also double the amount of new heap memory that application will allocate each cycle, which captures heap memory overheads. Note that _Live heap + GC roots_ is an approximation of the amount of memory the GC needs to scan.
Next, let's look at GC CPU cost. Total cost can be broken down as the cost per cycle, times GC frequency over some time period T.
_Total GC CPU cost = (GC CPU cost per cycle) * (GC frequency) * T_
GC CPU cost per cycle can be derived from the [GC model](https://go.dev/doc/gc-guide#Understanding_costs):
_GC CPU cost per cycle = (Live heap + GC roots) * (Cost per byte) + Fixed cost_
Note that sweep phase costs are ignored here as mark and scan costs dominate.
The steady state is defined by a constant allocation rate and a constant cost per byte, so in the steady state we can derive a GC frequency from this new heap memory:
_GC frequency = (Allocation rate) / (New heap memory) = (Allocation rate) / ((Live heap + GC roots) * GOGC / 100)_
Putting this together, we get the full equation for the total cost:
_Total GC CPU cost = (Allocation rate) / ((Live heap + GC roots) * GOGC / 100) * ((Live heap + GC roots) * (Cost per byte) + Fixed cost) * T_
For a sufficiently large heap (which represents most cases), the marginal costs of a GC cycle dominate the fixed costs. This allows for a significant simplification of the total GC CPU cost formula.
_Total GC CPU cost = (Allocation rate) / (GOGC / 100) * (Cost per byte) * T_
From this simplified formula, we can see that if we double GOGC, we halve total GC CPU cost. (Note that the visualizations in this guide do simulate fixed costs, so the GC CPU overheads reported by them will not exactly halve when GOGC doubles.) Furthermore, GC CPU costs are largely determined by allocation rate and the cost per byte to scan memory. For more information on how to reduce these costs specifically, see the [optimization guide](https://go.dev/doc/gc-guide#Optimization_guide).
Note: there exists a discrepancy between the size of the live heap, and the amount of that memory the GC actually needs to scan: the same size live heap but with a different structure will result in a different CPU cost, but the same memory cost, resulting a different trade-off. This is why the structure of the heap is part of the definition of the steady state. The heap target should arguably only include the scannable live heap as a closer approximation of memory the GC needs to scan, but this leads to degenerate behavior when there's a very small amount of scannable live heap but the live heap is otherwise large.
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
