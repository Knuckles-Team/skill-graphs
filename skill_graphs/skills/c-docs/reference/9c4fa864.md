## C++ standard library
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#correctness-improvements)
### Correctness Improvements
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-rtm-version-150)
##### Visual Studio 2017 RTM (version 15.0)
  * Minor `basic_string` `_ITERATOR_DEBUG_LEVEL != 0` diagnostics improvements. When an IDL check gets tripped in string machinery, it now reports the specific behavior that caused the trip. For example, instead of "string iterator not dereferenceable" you get "cannot dereference string iterator because it is out of range (e.g. an end iterator)".
  * Fixed the `std::promise` move assignment operator, which previously could cause code to block forever.
  * Fixed compiler errors with the `atomic<T*>` implicit conversion to `T*`.
  * `pointer_traits<Ptr>` now correctly detects `Ptr::rebind<U>`.
  * Fixed a missing **`const`**qualifier in the`move_iterator` subtraction operator.
  * Fixed silent bad codegen for stateful user-defined allocators requesting `propagate_on_container_copy_assignment` and `propagate_on_container_move_assignment`.
  * `atomic<T>` now tolerates overloaded `operator&()`.
  * Slightly improved compiler diagnostics for incorrect `bind()` calls.


There are more standard library improvements in Visual Studio 2017 RTM. For a complete list, see the C++ Team Blog entry [Standard Library Fixes In VS 2017 RTM](https://devblogs.microsoft.com/cppblog/stl-fixes-in-vs-2017-rtm/).
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-153-2)
##### Visual Studio 2017 version 15.3
  * Standard library containers now clamp their `max_size()` to `numeric_limits<difference_type>::max()` rather than the `max()` of `size_type`. This change ensures that the result of `distance()` on iterators from that container is representable in the return type of `distance()`.
  * Fixed missing specialization `auto_ptr<void>`.
  * The `for_each_n()`, `generate_n()`, and `search_n()` algorithms previously failed to compile if the length argument wasn't an integral type. They now attempt to convert nonintegral lengths to the iterators' `difference_type`.
  * `normal_distribution<float>` no longer emits warnings inside the standard library about narrowing from double to float.
  * Fixed some `basic_string` operations that used `npos` instead of `max_size()` when checking for maximum size overflow.
  * `condition_variable::wait_for(lock, relative_time, predicate)` would wait for the entire relative time if there was a spurious wake. Now it waits for only a single interval of the relative time.
  * `future::get()` now invalidates the `future`, as the standard requires.
  * `iterator_traits<void *>` used to be a hard error because it attempted to form `void&`; it now cleanly becomes an empty struct to allow use of `iterator_traits` in "is iterator" SFINAE conditions.
  * Some warnings reported by Clang **`-Wsystem-headers`**were fixed.
  * Also fixed "exception specification in declaration does not match previous declaration" reported by Clang **`-Wmicrosoft-exception-spec`**.
  * Also fixed mem-initializer-list ordering warnings reported by Clang and C1XX.
  * The unordered containers didn't swap their hash functions or predicates when the containers themselves were swapped. Now they do.
  * Many container swap operations are now marked **`noexcept`**(as our standard library never intends to throw an exception when detecting the non-`propagate_on_container_swap` non-equal-allocator undefined behavior condition).
  * Many `vector<bool>` operations are now marked **`noexcept`**.
  * The standard library now enforces matching allocator `value_type` (in C++17 mode) with an opt-out escape hatch.
  * Fixed some conditions where self-range-insert into `basic_string` would scramble the strings contents. (Note: self-range-insert into vectors is still prohibited by the Standard.)
  * `basic_string::shrink_to_fit()` is no longer affected by the allocator's `propagate_on_container_swap`.
  * `std::decay` now handles abominable function types, that is, function types that are cv-qualified, ref-qualified, or both.
  * Changed include directives to use proper case sensitivity and forward slashes, improving portability.
  * Fixed warning C4061 "enumerator '_enumerator_ ' in switch of enum '_enumeration_ ' is not explicitly handled by a case label." This warning is off-by-default and was fixed as an exception to the standard library's general policy for warnings. (The standard library is **`/W4`**clean, but doesn't attempt to be**`/Wall`**clean. Many off-by-default warnings are unusually noisy, and aren't intended to be used on a regular basis.)
  * Improved `std::list` debug checks. List iterators now check `operator->()`, and `list::unique()` now marks iterators as invalidated.
  * Fixed uses-allocator metaprogramming in `tuple`.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-155-2)
##### Visual Studio 2017 version 15.5
  * `std::partition` now calls the predicate `N` times instead of `N + 1` times, as the standard requires.
  * Attempts to avoid magic statistics in version 15.3 are repaired in version 15.5.
  * `std::atomic<T>` no longer requires `T` to be default constructible.
  * Heap algorithms that take logarithmic time behave differently when iterator debugging is enabled. They no longer do a linear time assertion that the input is in fact a heap.
  * `__declspec(allocator)` is now guarded for C1XX only, to prevent warnings from Clang, which doesn't understand this declspec.
  * `basic_string::npos` is now available as a compile time constant.
  * `std::allocator` in C++17 mode now properly handles allocation of over-aligned types, that is, types whose alignment is greater than `max_align_t`, unless disabled by **`/Zc:alignedNew-`**. For example, vectors of objects with 16-byte or 32-byte alignment are now properly aligned for SSE and AVX instructions.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#conformance-improvements)
### Conformance improvements
  * We added <any>, <string_view>, `apply()`, `make_from_tuple()`.
  * Added <optional>, <variant>, `shared_ptr::weak_type`, and <cstdalign>.
  * Enabled C++14 **`constexpr`**in`min(initializer_list)` , `max(initializer_list)`, and `minmax(initializer_list)`, and `min_element()`, `max_element()`, and `minmax_element()`.


For more information, see [Microsoft C/C++ language conformance](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170).
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-153-3)
##### Visual Studio 2017 version 15.3
  * Several other C++17 features have been implemented. For more information, see [Microsoft C++ language conformance table](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#improvements_153).
  * Implemented P0602R0 "variant and optional should propagate copy/move triviality".
  * The standard library now officially tolerates dynamic RTTI being disabled via the [/GR-](https://learn.microsoft.com/en-us/cpp/build/reference/gr-enable-run-time-type-information?view=msvc-170) option. Both `dynamic_pointer_cast()` and `rethrow_if_nested()` inherently require **`dynamic_cast`**, so the standard library now marks them as`=delete` under **`/GR-`**.
  * Even when dynamic RTTI is disabled via **`/GR-`**, "static RTTI" in the form of`typeid(SomeType)` is still available, and powers several standard library components. The standard library now supports disabling this feature too, via **`/D_HAS_STATIC_RTTI=0`**. This flag also disables`std::any` , the `target()` and `target_type()` member functions of `std::function`, and the `get_deleter()` friend member function of `std::shared_ptr` and `std::weak_ptr`.
  * The standard library now uses C++14 **`constexpr`**unconditionally, instead of conditionally defined macros.
  * The standard library now uses alias templates internally.
  * The standard library now uses **`nullptr`**internally, instead of`nullptr_t{}`. (Internal usage of NULL is eradicated. Internal usage of 0-as-null is being cleaned up gradually.)
  * The standard library now uses `std::move()` internally, instead of stylistically misusing `std::forward()`.
  * Changed `static_assert(false, "message")` to `#error message`. This change improves compiler diagnostics because `#error` immediately stops compilation.
  * The standard library no longer marks functions as `__declspec(dllimport)`. Modern linker technology no longer requires it.
  * Extracted SFINAE to default template arguments, which reduced clutter compared to return types and function argument types.
  * Debug checks in <random> now use the standard library's usual machinery, instead of the internal function `_Rng_abort()`, which called `fputs()` to `stderr`. This function's implementation is kept for binary compatibility. We'll remove it in the next binary-incompatible version of the standard library.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-155-3)
##### Visual Studio 2017 version 15.5
  * Several standard library features have been added, deprecated, or removed per the C++17 standard. For more information, see [C++ conformance improvements in Visual Studio](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#improvements_155).
  * Experimental support for the following parallel algorithms:
    * `all_of`
    * `any_of`
    * `for_each`
    * `for_each_n`
    * `none_of`
    * `reduce`
    * `replace`
    * `replace_if`
    * `sort`
  * The signatures for the following parallel algorithms are added but not parallelized at this time. Profiling showed no benefit in parallelizing algorithms that only move or permute elements:
    * `copy`
    * `copy_n`
    * `fill`
    * `fill_n`
    * `move`
    * `reverse`
    * `reverse_copy`
    * `rotate`
    * `rotate_copy`
    * `swap_ranges`


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-156)
##### Visual Studio 2017 version 15.6
  * `<memory_resource>`
  * Library Fundamentals V1
  * Deleting `polymorphic_allocator` assignment
  * Improving class template argument deduction


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-157-2)
##### Visual Studio 2017 version 15.7
  * Support for parallel algorithms is no longer experimental
  * A new implementation of `<filesystem>`
  * Elementary string conversions (partial)
  * `std::launder()`
  * `std::byte`
  * `hypot(x,y,z)`
  * Avoiding unnecessary decay
  * Mathematical special functions
  * `constexpr char_traits`
  * Deduction guides for the standard library


For more information, see [Microsoft C/C++ language conformance](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170).
[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#performance-and-throughput-fixes)
### Performance and throughput fixes
  * Made `basic_string::find(char)` overloads only call `traits::find` once. Previously, it was implemented as a general string search for a string of length 1.
  * `basic_string::operator==` now checks the string's size before comparing the strings' contents.
  * Removed control coupling in `basic_string`, which was difficult for the compiler optimizer to analyze. For all short strings, calling `reserve` still has a nonzero cost to do nothing.
  * `std::vector` was overhauled for correctness and performance: aliasing during insert and emplace operations is now correctly handled as required by the Standard, the strong exception guarantee is now provided when required by the Standard via `move_if_noexcept()` and other logic, and insert and emplace do fewer element operations.
  * The C++ standard library now avoids dereferencing null fancy pointers.
  * Improved `weak_ptr::lock()` performance.
  * To increase compiler throughput, C++ standard library headers now avoid including declarations for unnecessary compiler intrinsics.
  * Improved the performance of `std::string` and `std::wstring` move constructors by more than three times.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-153-4)
##### Visual Studio 2017 version 15.3
  * Worked around interactions with **`noexcept`**, which prevented inlining the`std::atomic` implementation into functions that use Structured Exception Handling (SHE).
  * Changed the standard library's internal `_Deallocate()` function to optimize into smaller code, allowing it to be inlined into more places.
  * Changed `std::try_lock()` to use pack expansion instead of recursion.
  * Improved the `std::lock()` deadlock avoidance algorithm to use `lock()` operations instead of spinning on `try_lock()` on all the locks.
  * Enabled the Named Return Value Optimization in `system_category::message()`.
  * `conjunction` and `disjunction` now instantiate `N + 1` types, instead of `2N + 2` types.
  * `std::function` no longer instantiates allocator support machinery for each type-erased callable, improving throughput and reducing .obj size in programs that pass many distinct lambdas to `std::function`.
  * `allocator_traits<std::allocator>` contains manually inlined `std::allocator` operations, reducing code size in code that interacts with `std::allocator` through `allocator_traits` only (that is, in most code).
  * The C++11 minimal allocator interface is now handled by the standard library calling `allocator_traits` directly, instead of wrapping the allocator in an internal class `_Wrap_alloc`. This change reduces the code size generated for allocator support, improves the optimizer's ability to reason about standard library containers in some cases, and provides a better debugging experience (as now you see your allocator type, rather than `_Wrap_alloc<your_allocator_type>` in the debugger).
  * Removed metaprogramming for customized `allocator::reference`, which allocators aren't allowed to customize. (Allocators can make containers use fancy pointers but not fancy references.)
  * The compiler front end was taught to unwrap debug iterators in range-based for loops, improving the performance of debug builds.
  * The `basic_string` internal shrink path for `shrink_to_fit()` and `reserve()` is no longer in the path of reallocating operations, reducing code size for all mutating members.
  * The `basic_string` internal grow path is no longer in the path of `shrink_to_fit()`.
  * The `basic_string` mutating operations are now factored into non-allocating fast path and allocating slow path functions, making it more likely for the common no-reallocate case to be inlined into callers.
  * The `basic_string` mutating operations now construct reallocated buffers in the preferred state rather than resizing in place. For example, an insert at the beginning of a string now moves the content after the insertion exactly once. It's moved either down or to the newly allocated buffer. It's no longer moved twice in the reallocating case, first to the newly allocated buffer and then down.
  * Operations calling the C standard library in <string> now cache the `errno` address to remove repeated interaction with TLS.
  * Simplified the `is_pointer` implementation.
  * Finished changing function-based Expression SFINAE to **`struct`**and`void_t` -based.
  * Standard library algorithms now avoid postincrementing iterators.
  * Fixed truncation warnings when using 32-bit allocators on 64-bit systems.
  * `std::vector` move assignment is now more efficient in the non-POCMA non-equal-allocator case, by reusing the buffer when possible.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#visual-studio-2017-version-155-4)
##### Visual Studio 2017 version 15.5
  * `basic_string<char16_t>` now engages the same `memcmp`, `memcpy`, and similar optimizations that `basic_string<wchar_t>` engages.
  * An optimizer limitation that prevented function pointers from being inlined, exposed by our "avoid copying functions" work in Visual Studio 2015 Update 3, has been worked around, restoring performance of `lower_bound(iter, iter, function pointer)`.
  * The overhead of iterator debugging's order verification of inputs to `includes`, `set_difference`, `set_symmetric_difference`, and `set_union` was reduced by unwrapping iterators before checking order.
  * `std::inplace_merge` now skips over elements that are already in position.
  * Constructing `std::random_device` no longer constructs and then destroys a `std::string`.
  * `std::equal` and `std::partition` had a jump-threading optimization pass that saves an iterator comparison.
  * When `std::reverse` is passed pointers to trivially copyable `T`, it now dispatches to a handwritten vectorized implementation.
  * `std::fill`, `std::equal`, and `std::lexicographical_compare` were taught how to dispatch to `memset` and `memcmp` for `std::byte` and `gsl::byte` (and other char-like enums and enum classes). Since `std::copy` dispatches using `is_trivially_copyable`, it didn't need any changes.
  * The standard library no longer contains empty-braces destructors whose only behavior was to make types non-trivially-destructible.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2017?view=msvc-170#other-libraries)
