## What's new for C++ in Visual Studio version 17.0
_Released Nov 2021_
Expand table
For more information about | See
---|---
New features in the Visual Studio 17.0 IDE | [Visual Studio 2022 version 17.0 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.0)
Standard Library (STL) merged C++23 and C++26 features, C++20 defect reports, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
C++ language conformance improvements in Visual Studio 2022 17.0 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022 17.10](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_170)
An overview of some of the new features in Visual Studio 2022 version 17.0:
  * The Visual Studio IDE, _`devenv.exe`_, is now a native 64-bit application.
  * The MSVC toolset now defaults to SHA-256 source hashing in debug records. Previously, the toolset used MD5 for source hashing by default.
  * The v143 build tools are now available through the Visual Studio installer and in the


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#hot-reload-for-native-c)
### Hot Reload for native C++
  * [Hot Reload for C++](https://devblogs.microsoft.com/cppblog/edit-your-c-code-while-debugging-with-hot-reload-in-visual-studio-2022/) makes it possible to make many types of code edits to your running app and apply them without needing to pause app execution with something like a breakpoint.


In Visual Studio 2022, when you start your app in the debugger, you can use the Hot Reload button to modify your application while it's still running. This experience is powered by native Edit and Continue. For more information about supported edits, see [Edit and Continue (C++)](https://learn.microsoft.com/en-us/visualstudio/debugger/edit-and-continue-visual-cpp?view=vs-2022&preserve-view=true).
  * Hot Reload supports CMake and Open Folder projects.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#wsl2-support)
### WSL2 support
  * You can now build and debug natively on WSL2 without establishing an SSH connection. Both cross-platform CMake projects and MSBuild-based Linux projects are supported.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#improved-cmake-support)
### Improved CMake support
  * Upgraded the version of CMake shipped with Visual Studio to version 3.21. For more information on what's available in this version, see the
  * CMake Overview Pages are updated to support _`CMakePresets.json`_.
  * You can now configure and build your CMake projects with CMake 3.21 and _`CMakePresets.json`_v3.
  * Visual Studio now supports the `buildPresets.targets` option in _`CMakePresets.json`_. This option allows you to build a subset of targets in your CMake project.
  * The Project menu in CMake projects is streamlined and exposes options to "Delete Cache and Reconfigure" and "View Cache."
  * Implemented the **`/scanDependencies`**compiler option to list C++20 module dependencies for CMake projects, as described in


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#standard-library-improvements)
### Standard Library improvements
Select Standard Library (STL) improvements are highlighted here. For a comprehensive list of new functionality, changes, bug fixes, and performance improvements, see the STL team's
  * Added debugging visualizers to improve how the following types are displayed: `source_location`, `bind_front()`, `u8string` (and its iterators), `default_sentinel_t`, `unreachable_sentinel_t`, `ranges::empty_view`, `ranges::single_view`, `ranges::iota_view` (and its iterator/sentinel), `ranges::ref_view`, `thread`, `thread::id`, `jthread`, and `filesystem::path`
  * Added `[[nodiscard]]` to the `stoi()` family of functions in `<string>` and to various functions in `<locale>` such as the `collate` member functions, `has_facet()`, and the `isalnum()` and `tolower()` families.
  * `std::string` `constexpr` in VS 2019 16.10. Now supported for Clang.
  * `std::vector` `constexpr` in VS 2019 16.10. Now supported for Clang.


**Highlighted C++23 features**
  * `is_scoped_enum`, a new trait for the C++ Standard library, which detects whether a type is a scoped enumeration.
  * `out_ptr()`, `inout_ptr()`
  * `contains()` For `basic_string` and `basic_string_view`
  * `to_underlying()` for enumerations
  * `std::variant`
  * `basic_string` and `basic_string_view` from `nullptr`. This change is a source-breaking change. Code that previously had undefined behavior at runtime is now rejected with compiler errors.
  * `declare_reachable`, `undeclare_reachable`, `declare_no_pointers`, `undeclare_no_pointers`, `get_pointer_safety`. Previously, these functions had no effect.


**Highlighted performance improvements**
  * `<format>` now detects when it's writing to a `back_insert_iterator` for a `basic_string` or a `vector`, and makes a faster call to `insert()` at the `end()` of the container.
  * We improved the performance of `std::find()` and `std::count()` for `vector<bool>` 19x and 26x (times, not percent).
  * We improved the performance of `std::count()` for `vector<bool>`
  * `std::byte` now has the same performance as `unsigned char` in `reverse()` and `variant::swap()`


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#clang-and-llvm-support)
### Clang and LLVM support
  * LLVM tools shipped with Visual Studio are upgraded to LLVM 12. For more information, see the
  * Clang-cl support was updated to LLVM 12.
  * You can now debug processes running on a remote system from Visual Studio by using LLDB.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#c-amp-deprecated)
### C++ AMP deprecated
  * C++ AMP headers are now deprecated. Including `<amp.h>` in a C++ project generates build errors. To silence the errors, define `_SILENCE_AMP_DEPRECATION_WARNINGS`. For more information, see [our AMP Deprecation links](https://learn.microsoft.com/en-us/cpp/parallel/amp/cpp-amp-overview?view=msvc-170).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#intellisense-improvements)
### IntelliSense improvements
  * We made improvements in C++ IntelliSense when providing navigation and syntax highlighting for types from imported Modules and Header Units. IntelliSense is an active area of investment for us. Help us improve: Share your feedback on Developer Community by using **Help** > **Send Feedback**.
  * We improved C++ IntelliSense performance by optimizing cached header usage and symbol database access, providing improved load times to get into your code.
  * The IntelliSense Code Linter for C++ is now on by default, providing instant as-you-type suggestions and fix suggestions for common code defects.
  * C++ IntelliSense for CMake projects now works when using a preset with a display name.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#c-workload-updates)
### C++ Workload updates
  * Updated to NDK r21 LTS in the **C++ Mobile Development** workload.
  * The **Game development with C++** workload now installs the latest Unreal Engine with support for Visual Studio 2022.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#code-analysis-improvements)
### Code analysis improvements
  * Code analysis now enforces that return values of functions annotated with `_Check_return_` or `_Must_inspect_result_` must be checked.
  * Null pointer dereference detection is improved in our code analysis tooling.
  * Added support for `gsl::not_null` to code analysis.
  * Support for Libfuzzer under the **`/fsanitize=fuzzer`**compiler option.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#release-notes-for-older-versions)
