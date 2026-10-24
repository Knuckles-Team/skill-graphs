##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fthread&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fthread "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/thread.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/thread&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/thread.html)
##### Views
  * [View](https://en.cppreference.com/w/c/thread.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/thread.html)
# Concurrency support library
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")
[ C](https://en.cppreference.com/w/c.html "c")
[Compiler support](https://en.cppreference.com/w/c/compiler_support.html "c/compiler support")
---
[Language](https://en.cppreference.com/w/c/language.html "c/language")
[Headers](https://en.cppreference.com/w/c/header.html "c/header")
[Type support](https://en.cppreference.com/w/c/types.html "c/types")
[Program utilities](https://en.cppreference.com/w/c/program.html "c/program")
[Variadic function support](https://en.cppreference.com/w/c/variadic.html "c/variadic")
[Error handling](https://en.cppreference.com/w/c/error.html "c/error")
[Dynamic memory management](https://en.cppreference.com/w/c/memory.html "c/memory")
[Strings library](https://en.cppreference.com/w/c/string.html "c/string")
[Algorithms](https://en.cppreference.com/w/c/algorithm.html "c/algorithm")
[Numerics](https://en.cppreference.com/w/c/numeric.html "c/numeric")
[Date and time utilities](https://en.cppreference.com/w/c/chrono.html "c/chrono")
[Input/output support](https://en.cppreference.com/w/c/io.html "c/io")
[Localization support](https://en.cppreference.com/w/c/locale.html "c/locale")
**Concurrency support** (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
**Concurrency support library**
|  Threads
---
| [thrd_create](https://en.cppreference.com/w/c/thread/thrd_create.html "c/thread/thrd create")
---
[thrd_equal](https://en.cppreference.com/w/c/thread/thrd_equal.html "c/thread/thrd equal")
[thrd_current](https://en.cppreference.com/w/c/thread/thrd_current.html "c/thread/thrd current")
[thrd_sleep](https://en.cppreference.com/w/c/thread/thrd_sleep.html "c/thread/thrd sleep")
[thrd_yield](https://en.cppreference.com/w/c/thread/thrd_yield.html "c/thread/thrd yield")
[thrd_exit](https://en.cppreference.com/w/c/thread/thrd_exit.html "c/thread/thrd exit")
| [thrd_detach](https://en.cppreference.com/w/c/thread/thrd_detach.html "c/thread/thrd detach")
---
[thrd_join](https://en.cppreference.com/w/c/thread/thrd_join.html "c/thread/thrd join")
[thrd_successthrd_timedoutthrd_busythrd_nomemthrd_error](https://en.cppreference.com/w/c/thread/thrd_errors.html "c/thread/thrd errors")
Atomic operations
[atomic_init](https://en.cppreference.com/w/c/atomic/atomic_init.html "c/atomic/atomic init")
[ATOMIC_VAR_INIT](https://en.cppreference.com/w/c/atomic/ATOMIC_VAR_INIT.html "c/atomic/ATOMIC VAR INIT") (until C23)
[ATOMIC_***_LOCK_FREE](https://en.cppreference.com/w/c/atomic/ATOMIC_LOCK_FREE_consts.html "c/atomic/ATOMIC LOCK FREE consts")
[atomic_is_lock_free](https://en.cppreference.com/w/c/atomic/atomic_is_lock_free.html "c/atomic/atomic is lock free")
[atomic_store](https://en.cppreference.com/w/c/atomic/atomic_store.html "c/atomic/atomic store")
[atomic_load](https://en.cppreference.com/w/c/atomic/atomic_load.html "c/atomic/atomic load")
[atomic_exchange](https://en.cppreference.com/w/c/atomic/atomic_exchange.html "c/atomic/atomic exchange")
[atomic_compare_exchange](https://en.cppreference.com/w/c/atomic/atomic_compare_exchange.html "c/atomic/atomic compare exchange")
[atomic_fetch_add](https://en.cppreference.com/w/c/atomic/atomic_fetch_add.html "c/atomic/atomic fetch add")
[atomic_fetch_sub](https://en.cppreference.com/w/c/atomic/atomic_fetch_sub.html "c/atomic/atomic fetch sub")
[atomic_fetch_or](https://en.cppreference.com/w/c/atomic/atomic_fetch_or.html "c/atomic/atomic fetch or")
[atomic_fetch_xor](https://en.cppreference.com/w/c/atomic/atomic_fetch_xor.html "c/atomic/atomic fetch xor")
[atomic_fetch_and](https://en.cppreference.com/w/c/atomic/atomic_fetch_and.html "c/atomic/atomic fetch and")
|  Atomic flags
---
[atomic_flag](https://en.cppreference.com/w/c/atomic/atomic_flag.html "c/atomic/atomic flag")
[ATOMIC_FLAG_INIT](https://en.cppreference.com/w/c/atomic/ATOMIC_FLAG_INIT.html "c/atomic/ATOMIC FLAG INIT")
[atomic_flag_test_and_set](https://en.cppreference.com/w/c/atomic/atomic_flag_test_and_set.html "c/atomic/atomic flag test and set")
[atomic_flag_clear](https://en.cppreference.com/w/c/atomic/atomic_flag_clear.html "c/atomic/atomic flag clear")
Memory ordering
| [memory_order](https://en.cppreference.com/w/c/atomic/memory_order.html "c/atomic/memory order")
---
[kill_dependency](https://en.cppreference.com/w/c/atomic/kill_dependency.html "c/atomic/kill dependency")
| [atomic_thread_fence](https://en.cppreference.com/w/c/atomic/atomic_thread_fence.html "c/atomic/atomic thread fence")
---
[atomic_signal_fence](https://en.cppreference.com/w/c/atomic/atomic_signal_fence.html "c/atomic/atomic signal fence")
Mutual exclusion
| [mtx_init](https://en.cppreference.com/w/c/thread/mtx_init.html "c/thread/mtx init")
---
[mtx_lock](https://en.cppreference.com/w/c/thread/mtx_lock.html "c/thread/mtx lock")
[mtx_timedlock](https://en.cppreference.com/w/c/thread/mtx_timedlock.html "c/thread/mtx timedlock")
[mtx_trylock](https://en.cppreference.com/w/c/thread/mtx_trylock.html "c/thread/mtx trylock")
[call_once](https://en.cppreference.com/w/c/thread/ONCE_FLAG_INIT.html "c/thread/call once")
| [mtx_unlock](https://en.cppreference.com/w/c/thread/mtx_unlock.html "c/thread/mtx unlock")
---
[mtx_destroy](https://en.cppreference.com/w/c/thread/mtx_destroy.html "c/thread/mtx destroy")
[mtx_plainmtx_recursivemtx_timed](https://en.cppreference.com/w/c/thread/mtx_types.html "c/thread/mtx types")
Condition variables
| [cnd_init](https://en.cppreference.com/w/c/thread/cnd_init.html "c/thread/cnd init")
---
[cnd_signal](https://en.cppreference.com/w/c/thread/cnd_signal.html "c/thread/cnd signal")
[cnd_broadcast](https://en.cppreference.com/w/c/thread/cnd_broadcast.html "c/thread/cnd broadcast")
| [cnd_wait](https://en.cppreference.com/w/c/thread/cnd_wait.html "c/thread/cnd wait")
---
[cnd_timedwait](https://en.cppreference.com/w/c/thread/cnd_timedwait.html "c/thread/cnd timedwait")
[cnd_destroy](https://en.cppreference.com/w/c/thread/cnd_destroy.html "c/thread/cnd destroy")
Thread-local storage
| [thread_local](https://en.cppreference.com/w/c/thread/thread_local.html "c/thread/thread local")
---
[TSS_DTOR_ITERATIONS](https://en.cppreference.com/w/c/thread/TSS_DTOR_ITERATIONS.html "c/thread/TSS DTOR ITERATIONS")
[tss_create](https://en.cppreference.com/w/c/thread/tss_create.html "c/thread/tss create")
| [tss_get](https://en.cppreference.com/w/c/thread/tss_get.html "c/thread/tss get")
---
[tss_set](https://en.cppreference.com/w/c/thread/tss_set.html "c/thread/tss set")
[tss_delete](https://en.cppreference.com/w/c/thread/tss_delete.html "c/thread/tss delete")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/navbar_content&action=edit)
C includes built-in support for threads, atomic operations, mutual exclusion, condition variables, and thread-specific storages.
These features are optionally provided:
  * if the macro constant `__STDC_NO_THREADS__` is defined by the compiler, the header [`<threads.h>`](https://en.cppreference.com/w/c/header/threads.html "c/header/threads") and all of the names provided in it are not provided;
  * if the macro constant `__STDC_NO_ATOMICS__` is defined by the compiler, the header [`<stdatomic.h>`](https://en.cppreference.com/w/c/header/stdatomic.html "c/header/stdatomic") and all of the names provided in it are not provided.


See also [`**_Atomic**`type specifier and qualifier](https://en.cppreference.com/w/c/language/atomic.html "c/language/atomic").
## Contents
  * [1 Threads](https://en.cppreference.com/w/c/thread.html#Threads)
  * [2 Atomic operations](https://en.cppreference.com/w/c/thread.html#Atomic_operations)
    * [2.1 Operations on atomic types](https://en.cppreference.com/w/c/thread.html#Operations_on_atomic_types)
    * [2.2 Flag type and operations](https://en.cppreference.com/w/c/thread.html#Flag_type_and_operations)
    * [2.3 Initialization](https://en.cppreference.com/w/c/thread.html#Initialization)
    * [2.4 Memory synchronization ordering](https://en.cppreference.com/w/c/thread.html#Memory_synchronization_ordering)
    * [2.5 Convenience type aliases](https://en.cppreference.com/w/c/thread.html#Convenience_type_aliases)
  * [3 Mutual exclusion](https://en.cppreference.com/w/c/thread.html#Mutual_exclusion)
    * [3.1 Call once](https://en.cppreference.com/w/c/thread.html#Call_once)
  * [4 Condition variables](https://en.cppreference.com/w/c/thread.html#Condition_variables)
  * [5 Thread-local storage](https://en.cppreference.com/w/c/thread.html#Thread-local_storage)
  * [6 Reserved identifiers](https://en.cppreference.com/w/c/thread.html#Reserved_identifiers)
  * [7 References](https://en.cppreference.com/w/c/thread.html#References)
  * [8 See also](https://en.cppreference.com/w/c/thread.html#See_also)
  * [9 External links](https://en.cppreference.com/w/c/thread.html#External_links)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=1 "Edit section: Threads")] Threads
Defined in header `[`<threads.h>`](https://en.cppreference.com/w/c/header/threads.html "c/header/threads")`
---
`**thrd_t**` |  implementation-defined complete object type identifying a thread [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_t&action=edit)
[ thrd_create](https://en.cppreference.com/w/c/thread/thrd_create.html "c/thread/thrd create") (C11) |  creates a thread
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_create&action=edit)
[ thrd_equal](https://en.cppreference.com/w/c/thread/thrd_equal.html "c/thread/thrd equal") (C11) |  checks if two identifiers refer to the same thread
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_equal&action=edit)
[ thrd_current](https://en.cppreference.com/w/c/thread/thrd_current.html "c/thread/thrd current") (C11) |  obtains the current thread identifier
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_current&action=edit)
[ thrd_sleep](https://en.cppreference.com/w/c/thread/thrd_sleep.html "c/thread/thrd sleep") (C11) |  suspends execution of the calling thread for the given period of time
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_sleep&action=edit)
[ thrd_yield](https://en.cppreference.com/w/c/thread/thrd_yield.html "c/thread/thrd yield") (C11) |  yields the current time slice
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_yield&action=edit)
[ thrd_exit](https://en.cppreference.com/w/c/thread/thrd_exit.html "c/thread/thrd exit") (C11) |  terminates the calling thread
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_exit&action=edit)
[ thrd_detach](https://en.cppreference.com/w/c/thread/thrd_detach.html "c/thread/thrd detach") (C11) |  detaches a thread
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_detach&action=edit)
[ thrd_join](https://en.cppreference.com/w/c/thread/thrd_join.html "c/thread/thrd join") (C11) |  blocks until a thread terminates
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_join&action=edit)
[ thrd_successthrd_timedoutthrd_busythrd_nomemthrd_error](https://en.cppreference.com/w/c/thread/thrd_errors.html "c/thread/thrd errors") (C11) |  indicates a thread error status
(constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_errors&action=edit)
thrd_start_t (C11) |  a typedef of the function pointer type int(*)(void*), used by [thrd_create](https://en.cppreference.com/w/c/thread/thrd_create.html)
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thrd_start_t&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=2 "Edit section: Atomic operations")] Atomic operations
Defined in header `[`<stdatomic.h>`](https://en.cppreference.com/w/c/header/stdatomic.html "c/header/stdatomic")`
---
#####  Operations on atomic types
[ ATOMIC_BOOL_LOCK_FREEATOMIC_CHAR_LOCK_FREEATOMIC_CHAR16_T_LOCK_FREEATOMIC_CHAR32_T_LOCK_FREEATOMIC_WCHAR_T_LOCK_FREEATOMIC_SHORT_LOCK_FREEATOMIC_INT_LOCK_FREEATOMIC_LONG_LOCK_FREEATOMIC_LLONG_LOCK_FREEATOMIC_POINTER_LOCK_FREE](https://en.cppreference.com/w/c/atomic/ATOMIC_LOCK_FREE_consts.html "c/atomic/ATOMIC LOCK FREE consts") (C11) |  indicates that the given atomic type is lock-free
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_ATOMIC_LOCK_FREE_consts&action=edit)
[ atomic_is_lock_free](https://en.cppreference.com/w/c/atomic/atomic_is_lock_free.html "c/atomic/atomic is lock free") (C11) |  indicates whether the atomic object is lock-free
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_is_lock_free&action=edit)
[ atomic_storeatomic_store_explicit](https://en.cppreference.com/w/c/atomic/atomic_store.html "c/atomic/atomic store") (C11) |  stores a value in an atomic object
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_store&action=edit)
[ atomic_loadatomic_load_explicit](https://en.cppreference.com/w/c/atomic/atomic_load.html "c/atomic/atomic load") (C11) |  reads a value from an atomic object
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_load&action=edit)
[ atomic_exchangeatomic_exchange_explicit](https://en.cppreference.com/w/c/atomic/atomic_exchange.html "c/atomic/atomic exchange") (C11) |  swaps a value with the value of an atomic object
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_exchange&action=edit)
[ atomic_compare_exchange_strongatomic_compare_exchange_strong_explicitatomic_compare_exchange_weakatomic_compare_exchange_weak_explicit](https://en.cppreference.com/w/c/atomic/atomic_compare_exchange.html "c/atomic/atomic compare exchange") (C11) |  swaps a value with an atomic object if the old value is what is expected, otherwise reads the old value
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_compare_exchange&action=edit)
[ atomic_fetch_addatomic_fetch_add_explicit](https://en.cppreference.com/w/c/atomic/atomic_fetch_add.html "c/atomic/atomic fetch add") (C11) |  atomic addition
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_fetch_add&action=edit)
[ atomic_fetch_subatomic_fetch_sub_explicit](https://en.cppreference.com/w/c/atomic/atomic_fetch_sub.html "c/atomic/atomic fetch sub") (C11) |  atomic subtraction
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_fetch_sub&action=edit)
[ atomic_fetch_oratomic_fetch_or_explicit](https://en.cppreference.com/w/c/atomic/atomic_fetch_or.html "c/atomic/atomic fetch or") (C11) |  atomic bitwise OR
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_fetch_or&action=edit)
[ atomic_fetch_xoratomic_fetch_xor_explicit](https://en.cppreference.com/w/c/atomic/atomic_fetch_xor.html "c/atomic/atomic fetch xor") (C11) |  atomic bitwise exclusive OR
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_fetch_xor&action=edit)
[ atomic_fetch_andatomic_fetch_and_explicit](https://en.cppreference.com/w/c/atomic/atomic_fetch_and.html "c/atomic/atomic fetch and") (C11) |  atomic bitwise AND
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_fetch_and&action=edit)
#####  Flag type and operations
[ atomic_flag](https://en.cppreference.com/w/c/atomic/atomic_flag.html "c/atomic/atomic flag") (C11) |  lock-free atomic boolean flag
(struct)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_flag&action=edit)
[ atomic_flag_test_and_setatomic_flag_test_and_set_explicit](https://en.cppreference.com/w/c/atomic/atomic_flag_test_and_set.html "c/atomic/atomic flag test and set") (C11) |  sets an atomic_flag to true and returns the old value
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_flag_test_and_set&action=edit)
[ atomic_flag_clearatomic_flag_clear_explicit](https://en.cppreference.com/w/c/atomic/atomic_flag_clear.html "c/atomic/atomic flag clear") (C11) |  sets an atomic_flag to false
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_flag_clear&action=edit)
#####  Initialization
[ atomic_init](https://en.cppreference.com/w/c/atomic/atomic_init.html "c/atomic/atomic init") (C11) |  initializes an existing atomic object
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_init&action=edit)
[ ATOMIC_VAR_INIT](https://en.cppreference.com/w/c/atomic/ATOMIC_VAR_INIT.html "c/atomic/ATOMIC VAR INIT") (C11)(deprecated in C17)(removed in C23) |  initializes a new atomic object
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_ATOMIC_VAR_INIT&action=edit)
[ ATOMIC_FLAG_INIT](https://en.cppreference.com/w/c/atomic/ATOMIC_FLAG_INIT.html "c/atomic/ATOMIC FLAG INIT") (C11) |  initializes a new [atomic_flag](https://en.cppreference.com/w/c/atomic/atomic_flag.html)
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_ATOMIC_FLAG_INIT&action=edit)
#####  Memory synchronization ordering
[ memory_order](https://en.cppreference.com/w/c/atomic/memory_order.html "c/atomic/memory order") (C11) |  defines memory ordering constraints
(enum) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_memory_order&action=edit)
[ kill_dependency](https://en.cppreference.com/w/c/atomic/kill_dependency.html "c/atomic/kill dependency") (C11) |  breaks a dependency chain for [memory_order_consume](https://en.cppreference.com/w/c/atomic/memory_order.html)
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_kill_dependency&action=edit)
[ atomic_thread_fence](https://en.cppreference.com/w/c/atomic/atomic_thread_fence.html "c/atomic/atomic thread fence") (C11) |  generic memory order-dependent fence synchronization primitive
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_thread_fence&action=edit)
[ atomic_signal_fence](https://en.cppreference.com/w/c/atomic/atomic_signal_fence.html "c/atomic/atomic signal fence") (C11) |  fence between a thread and a signal handler executed in the same thread
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/atomic/dsc_atomic_signal_fence&action=edit)
#####  Convenience type aliases
---
Typedef name  |  Full type name
`atomic_bool` (C11) |  _Atomic _Bool(until C23)_Atomic bool(since C23)
`atomic_char` (C11) |  _Atomic char
`atomic_schar` (C11) |  _Atomic signed char
`atomic_uchar` (C11) |  _Atomic unsigned char
`atomic_short` (C11) |  _Atomic short
`atomic_ushort` (C11) |  _Atomic unsigned short
`atomic_int` (C11) |  _Atomic int
`atomic_uint` (C11) |  _Atomic unsigned int
`atomic_long` (C11) |  _Atomic long
`atomic_ulong` (C11) |  _Atomic unsigned long
`atomic_llong` (C11) |  _Atomic long long
`atomic_ullong` (C11) |  _Atomic unsigned long long
`atomic_char8_t` (C23) |  _Atomic char8_t
`atomic_char16_t` (C11) |  _Atomic char16_t
`atomic_char32_t` (C11) |  _Atomic char32_t
`atomic_wchar_t` (C11) |  _Atomic wchar_t
`atomic_int_least8_t` (C11) |  _Atomic [int_least8_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uint_least8_t` (C11) |  _Atomic [uint_least8_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_int_least16_t` (C11) |  _Atomic [int_least16_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uint_least16_t` (C11) |  _Atomic [uint_least16_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_int_least32_t` (C11) |  _Atomic [int_least32_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uint_least32_t` (C11) |  _Atomic [uint_least32_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_int_least64_t` (C11) |  _Atomic [int_least64_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uint_least64_t` (C11) |  _Atomic [uint_least64_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_int_fast8_t` (C11) |  _Atomic [int_fast8_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uint_fast8_t` (C11) |  _Atomic [uint_fast8_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_int_fast16_t` (C11) |  _Atomic [int_fast16_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uint_fast16_t` (C11) |  _Atomic [uint_fast16_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_int_fast32_t` (C11) |  _Atomic [int_fast32_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uint_fast32_t` (C11) |  _Atomic [uint_fast32_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_int_fast64_t` (C11) |  _Atomic [int_fast64_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uint_fast64_t` (C11) |  _Atomic [uint_fast64_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_intptr_t` (C11) |  _Atomic [intptr_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uintptr_t` (C11) |  _Atomic [uintptr_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_size_t` (C11) |  _Atomic [size_t](https://en.cppreference.com/w/c/types/size_t.html)
`atomic_ptrdiff_t` (C11) |  _Atomic [ptrdiff_t](https://en.cppreference.com/w/c/types/ptrdiff_t.html)
`atomic_intmax_t` (C11) |  _Atomic [intmax_t](https://en.cppreference.com/w/c/types/integer.html)
`atomic_uintmax_t` (C11) |  _Atomic [uintmax_t](https://en.cppreference.com/w/c/types/integer.html)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=3 "Edit section: Mutual exclusion")] Mutual exclusion
Defined in header `[`<threads.h>`](https://en.cppreference.com/w/c/header/threads.html "c/header/threads")`
---
`**mtx_t**` |  mutex identifier [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_mtx_t&action=edit)
[ mtx_init](https://en.cppreference.com/w/c/thread/mtx_init.html "c/thread/mtx init") (C11) |  creates a mutex
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_mtx_init&action=edit)
[ mtx_lock](https://en.cppreference.com/w/c/thread/mtx_lock.html "c/thread/mtx lock") (C11) |  blocks until locks a mutex
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_mtx_lock&action=edit)
[ mtx_timedlock](https://en.cppreference.com/w/c/thread/mtx_timedlock.html "c/thread/mtx timedlock") (C11) |  blocks until locks a mutex or times out
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_mtx_timedlock&action=edit)
[ mtx_trylock](https://en.cppreference.com/w/c/thread/mtx_trylock.html "c/thread/mtx trylock") (C11) |  locks a mutex or returns without blocking if already locked
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_mtx_trylock&action=edit)
[ mtx_unlock](https://en.cppreference.com/w/c/thread/mtx_unlock.html "c/thread/mtx unlock") (C11) |  unlocks a mutex
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_mtx_unlock&action=edit)
[ mtx_destroy](https://en.cppreference.com/w/c/thread/mtx_destroy.html "c/thread/mtx destroy") (C11) |  destroys a mutex
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_mtx_destroy&action=edit)
[ mtx_plainmtx_recursivemtx_timed](https://en.cppreference.com/w/c/thread/mtx_types.html "c/thread/mtx types") (C11)(C11)(C11) |  defines the type of a mutex
(enum) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_mtx_types&action=edit)
#####  Call once
[ call_once](https://en.cppreference.com/w/c/thread/ONCE_FLAG_INIT.html "c/thread/call once") (C11) |  calls a function exactly once
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_call_once&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=4 "Edit section: Condition variables")] Condition variables
Defined in header `[`<threads.h>`](https://en.cppreference.com/w/c/header/threads.html "c/header/threads")`
---
`**cnd_t**` |  condition variable identifier
[ cnd_init](https://en.cppreference.com/w/c/thread/cnd_init.html "c/thread/cnd init") (C11) |  creates a condition variable
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_cnd_init&action=edit)
[ cnd_signal](https://en.cppreference.com/w/c/thread/cnd_signal.html "c/thread/cnd signal") (C11) |  unblocks one thread blocked on a condition variable
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_cnd_signal&action=edit)
[ cnd_broadcast](https://en.cppreference.com/w/c/thread/cnd_broadcast.html "c/thread/cnd broadcast") (C11) |  unblocks all threads blocked on a condition variable
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_cnd_broadcast&action=edit)
[ cnd_wait](https://en.cppreference.com/w/c/thread/cnd_wait.html "c/thread/cnd wait") (C11) |  blocks on a condition variable
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_cnd_wait&action=edit)
[ cnd_timedwait](https://en.cppreference.com/w/c/thread/cnd_timedwait.html "c/thread/cnd timedwait") (C11) |  blocks on a condition variable, with a timeout
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_cnd_timedwait&action=edit)
[ cnd_destroy](https://en.cppreference.com/w/c/thread/cnd_destroy.html "c/thread/cnd destroy") (C11) |  destroys a condition variable
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_cnd_destroy&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=5 "Edit section: Thread-local storage")] Thread-local storage
Defined in header `[`<threads.h>`](https://en.cppreference.com/w/c/header/threads.html "c/header/threads")`
---
[ thread_local](https://en.cppreference.com/w/c/thread/thread_local.html "c/thread/thread local") (C11)(removed in C23) |  convenience macro for storage-class specifier _Thread_local
(keyword macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_thread_local&action=edit)
`**tss_t**` |  thread-specific storage pointer [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_tss_t&action=edit)
[ TSS_DTOR_ITERATIONS](https://en.cppreference.com/w/c/thread/TSS_DTOR_ITERATIONS.html "c/thread/TSS DTOR ITERATIONS") (C11) |  maximum number of times destructors are called
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_TSS_DTOR_ITERATIONS&action=edit)
`**tss_dtor_t**`(C11) |  function pointer type void(*)(void*), used for TSS destructor
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_tss_dtor_t&action=edit)
[ tss_create](https://en.cppreference.com/w/c/thread/tss_create.html "c/thread/tss create") (C11) |  creates thread-specific storage pointer with a given destructor
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_tss_create&action=edit)
[ tss_get](https://en.cppreference.com/w/c/thread/tss_get.html "c/thread/tss get") (C11) |  reads from thread-specific storage
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_tss_get&action=edit)
[ tss_set](https://en.cppreference.com/w/c/thread/tss_set.html "c/thread/tss set") (C11) |  write to thread-specific storage
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_tss_set&action=edit)
[ tss_delete](https://en.cppreference.com/w/c/thread/tss_delete.html "c/thread/tss delete") (C11) |  releases the resources held by a given thread-specific pointer
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/thread/dsc_tss_delete&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=6 "Edit section: Reserved identifiers")] Reserved identifiers
In future revisions of the C standard:
  * function names, type names, and enumeration constants that begin with either `cnd_`, `mtx_`, `thrd_`, or `tss_`, and a lowercase letter may be added to the declarations in the `<threads.h>` header;
  * macros that begin with `ATOMIC_` and an uppercase letter may be added to the macros defined in the [`<stdatomic.h>`](https://en.cppreference.com/w/c/header/stdatomic.html "c/header/stdatomic") header;
  * typedef names that begin with either `atomic_` or `memory_`, and a lowercase letter may be added to the declarations in the [`<stdatomic.h>`](https://en.cppreference.com/w/c/header/stdatomic.html "c/header/stdatomic") header;
  * enumeration constants that begin with `memory_order_` and a lowercase letter may be added to the definition of the [memory_order](https://en.cppreference.com/w/c/atomic/memory_order.html "c/atomic/memory order") type in the [`<stdatomic.h>`](https://en.cppreference.com/w/c/header/stdatomic.html "c/header/stdatomic") header;
  * function names that begin with `atomic_` and a lowercase letter may be added to the declarations in the [`<stdatomic.h>`](https://en.cppreference.com/w/c/header/stdatomic.html "c/header/stdatomic") header.


Identifiers reserved for functions names are always potentially(since C23) reserved for use as identifiers with external linkage, while other identifiers list here are potentially(since C23) reserved when [`<stdatomic.h>`](https://en.cppreference.com/w/c/header/stdatomic.html "c/header/stdatomic") is included.
Declaring, defining, or #undefing such an identifier results in undefined behavior if it is provided by the standard or implementation(since C23). Portable programs should not use those identifiers.
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=7 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.17 Atomics <stdatomic.h> (p: TBD)


  * 7.26 Threads <threads.h> (p: TBD)


  * 7.31.8 Atomics <stdatomic.h> (p: TBD)


  * 7.31.15 Threads <threads.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.17 Atomics <stdatomic.h> (p: 200-209)


  * 7.26 Threads <threads.h> (p: 274-283)


  * 7.31.8 Atomics <stdatomic.h> (p: 332)


  * 7.31.15 Threads <threads.h> (p: 333)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.17 Atomics <stdatomic.h> (p: 273-286)


  * 7.26 Threads <threads.h> (p: 376-387)


  * 7.31.8 Atomics <stdatomic.h> (p: 455-456)


  * 7.31.15 Threads <threads.h> (p: 456)


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=8 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/atomic.html "cpp/thread") for Concurrency support library
---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=edit&section=9 "Edit section: External links")] External links
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/thread&oldid=180203](https://en.cppreference.com/mwiki/index.php?title=c/thread&oldid=180203)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/thread.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/thread "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/thread "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/thread&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/thread&oldid=180203 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/thread&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/thread "c/thread")
  * [Česky](http://cs.cppreference.com/w/c/thread "c/thread")
  * [Deutsch](http://de.cppreference.com/w/c/thread "c/thread")
  * [Español](http://es.cppreference.com/w/c/thread "c/thread")
  * [Français](http://fr.cppreference.com/w/c/thread "c/thread")
  * [Italiano](http://it.cppreference.com/w/c/thread "c/thread")
  * [日本語](http://ja.cppreference.com/w/c/thread "c/thread")
  * [한국어](http://ko.cppreference.com/w/c/thread "c/thread")
  * [Polski](http://pl.cppreference.com/w/c/thread "c/thread")
  * [Português](http://pt.cppreference.com/w/c/thread "c/thread")
  * [Русский](http://ru.cppreference.com/w/c/thread "c/thread")
  * [Türkçe](http://tr.cppreference.com/w/c/thread "c/thread")
  * [中文](http://zh.cppreference.com/w/c/thread "c/thread")


  * This page was last modified on 6 February 2025, at 16:27.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
