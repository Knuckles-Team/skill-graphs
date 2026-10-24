## What's new for C++ in Visual Studio version 17.4
_Released Nov 2022_
Expand table
For more information about | See
---|---
What's new for C++ developers | [What's New for C++ Developers in Visual Studio 2022 17.4](https://devblogs.microsoft.com/cppblog/whats-new-for-cpp-developers-in-visual-studio-2022-17-4/)
Standard Library (STL) merged C++23 features, Language Working Group (LWG) issue resolutions, performance improvements, enhanced behavior, and fixed bugs |
New features in the Visual Studio 17.4 IDE | [Visual Studio 2022 version 17.4 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes-v17.4)
C++ language conformance improvements in Visual Studio 2022 17.4 | [C++ Conformance improvements, behavior changes, and bug fixes in Visual Studio 2022](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_174)
A partial list of new features in 17.4:
  * Improved compiler error messages to provide more correct and useful information, especially for concepts.
  * Added experimental MSVC option [`/experimental:log<directory>`](https://learn.microsoft.com/en-us/cpp/build/reference/experimental-log?view=msvc-170) to output [structured SARIF diagnostics](https://learn.microsoft.com/en-us/cpp/build/reference/sarif-output?view=msvc-170) to the specified directory.
  * Added support for C23 attributes to IntelliSense and continued progress in C++20 modules support.
  * Improved indexing performance when opening a new solution. Large projects could see a 20-35% improvement from 17.3.
  * Improved Named Return Value Optimization (NRVO):
    * NRVO is enabled for cases that involve exception handling or loops.
    * NRVO is enabled even under **`/Od`**if the user passes the**`/Zc:nrvo`**option, or**`/std:c++20`**or later, or**`/permissive-`**.
    * You can now disable NRVO with the **`/Zc:nrvo-`**option.
  * Upgraded the version of LLVM shipped with Visual Studio to 15.0.1. For more information on what is available, see the
  * Added support to Visual Studio for vcpkg artifacts with CMake projects. For projects that include a vcpkg manifest, the environment is activated automatically on project open. Learn more about this feature in the
  * You can now use Dev Containers for your C++ projects. Learn more about this feature in our
  * IntelliSense now respects the order of preincluded headers when one of them is a PCH. Previously, when a PCH was used via **`/Yu`**and force-included via**`/FI`**, IntelliSense would always process it first, before any other headers included via**`/FI`**. This behavior didn't match the build behavior. With this change,**`/FI`**headers are processed in the order they're specified.
  * Removed internal prefixes from CTest names in Test Explorer.
  * Updated the version of CMake shipped with Visual Studio to version 3.24.1. For details of what is available, see the
  * Android SDK update:
    * Ant scripts were removed, so users no longer see Ant-based templates in the New Project dialog. For help migrating from Ant templates to Gradle templates, see
    * Added support for building with NDK 23 and 24
    * Updated NDK component to the LTS version 23
  * Added vectorized implementations of `ranges::min_element()`, `ranges::max_element()`, and `ranges::minmax_element()`
  * We continue to track the latest developments in C++ standardization. Support for these C++23 features is available by including [`/std:c++latest`](https://learn.microsoft.com/en-us/cpp/build/reference/std-specify-language-standard-version?view=msvc-170) in your compiler options:
    * `ranges::contains`, `ranges::contains_subrange`
    * `string_view` Range Constructor Should Be `explicit`
    * `auto(x)`: decay-copy In The Language
(The compiler part isn't implemented yet. The library part was implemented in C++20 mode when Ranges support was initially implemented.)
    * `<stacktrace>`
    * `pmr` alias for `std::stacktrace`
    * `constexpr type_info::operator==()`
    * `ranges::iota`, `ranges::shift_left`, `ranges::shift_right`
    * `views::join_with`
  * Added an option "Navigation after Create Declaration/Definition" to allow you to choose the navigation behavior of the Create Declaration/Definition feature. You can select between peeking (the default) or opening the document, or no navigation.
  * Arm64 builds of Visual Studio now bundle Arm64 versions of CMake and Ninja.
  * Added support for CMake Presets version 4. For details of what is available, see the
  * Remote system connections using the [Connection Manager](https://learn.microsoft.com/en-us/cpp/linux/connect-to-your-remote-linux-computer?view=msvc-170) now support SSH ProxyJump. ProxyJump is used to access an SSH host via another SSH host (for example, to access a host behind a firewall).


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-visual-cpp-in-visual-studio?view=msvc-170#whats-new-for-c-in-visual-studio-version-173)
