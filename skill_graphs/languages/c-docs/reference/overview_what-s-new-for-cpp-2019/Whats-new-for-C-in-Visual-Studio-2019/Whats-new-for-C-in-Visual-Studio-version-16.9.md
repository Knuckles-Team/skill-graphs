## What's new for C++ in Visual Studio version 16.9
For a summary of new features and bug fixes in Visual Studio version 16.9, see [What's New in Visual Studio 2019 version 16.9](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes-v16.9).
  * [Address Sanitizer](https://learn.microsoft.com/en-us/cpp/sanitizers/asan?view=msvc-170):
    * Our address sanitizer support on Windows is out of experimental mode and has reached general availability.
    * Expanded `RtlAllocateHeap` support, fixed a compatibility issue with `RtlCreateHeap` and `RtlAllocateHeap` interceptors when creating executable memory pools.
    * Added support for the legacy `GlobalAlloc` and `LocalAlloc` family of memory functions. You can enable these interceptors by setting the environment flag `ASAN_OPTIONS=windows_hook_legacy_allocators=true`.
    * Updated error messages for shadow memory interleaving and interception failure to make problems and resolutions explicit.
    * The IDE integration can now handle the complete collection of exceptions which ASan can report.
    * The compiler and linker will suggest emitting debug information if they detect you're building with ASan but not emitting debug information.
  * You can now target the LLVM version of the OpenMP runtime with the new CL switch **`/openmp:llvm`**. This adds support for the`lastprivate` clause on `#pragma omp` sections and unsigned index variables in parallel `for` loops. The **`/openmp:llvm`**switch is currently only available for the amd64 target and is still experimental.
  * Visual Studio CMake projects now have first-class support for remote Windows development. This includes configuring a CMake project to target Windows ARM64, deploying the project to a remote Windows machine, and debugging the project on a remote Windows machine from Visual Studio.
  * The version of Ninja shipped with Visual Studio on Windows has been updated to version 1.10. For more information on what's included, see the
  * The version of CMake shipped with Visual Studio has been updated to version 3.19. For more information on what's included, see the
  * IntelliSense:
    * Improved the stability and functionality of providing imported modules and header units completion in IntelliSense.
    * Added Go-to-definition on module imports, indexing support for `export {...}`, and more accurate module reference for modules with the same name.
    * Improved the language conformance of C++ IntelliSense by adding support for `__builtin_memcpy` and `__builtin_memmove`,
    * Added completion for make_unique, make_shared, emplace and emplace_back which provides completion based on the type parameter specified.
  * MSVC now determines the correct address sanitizer runtimes required for your binaries. Your Visual Studio project will automatically get the new changes. When using address sanitizer on the command line, you now only need to pass [`/fsanitize=address`](https://learn.microsoft.com/en-us/cpp/build/reference/fsanitize?view=msvc-170) to the compiler.
  * Visual Studio's Connection Manager now supports private keys using the ECDSA public key algorithm.
  * Updated the versions of LLVM and Clang shipped in our installer to v11. Read the release notes for
  * Visual Studio will now use CMake variables from toolchain files to configure IntelliSense. This will provide a better experience for embedded and Android development.
  * Implementation of the **`constexpr`**. This paves the way for utilities like**`constexpr`**`std::vector` and `std::string`.
  * Extended support for C++20 modules IntelliSense, including Go To Definition, Go To Module, and member completion.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#whats-new-for-c-in-visual-studio-version-168)
