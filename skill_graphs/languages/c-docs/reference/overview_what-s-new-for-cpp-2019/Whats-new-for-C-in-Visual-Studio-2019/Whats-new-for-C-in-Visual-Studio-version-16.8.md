## What's new for C++ in Visual Studio version 16.8
For a summary of new features and bug fixes in Visual Studio version 16.8, see [What's New in Visual Studio 2019 version 16.8](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes-v16.8).
  * C++20 Coroutines are now supported under [`/std:c++latest`](https://learn.microsoft.com/en-us/cpp/build/reference/std-specify-language-standard-version?view=msvc-170) (or **`/std:c++20`**starting in Visual Studio 2019 version 16.11) and the`<coroutine>` header.
  * IntelliSense now provides support for C++20 `<concepts>` and `<ranges>` headers, and rename and browsing for concept definitions.
  * Our STL now has support for the majority of C++20 Ranges.
  * C11 and C17 are now supported under the [`/std:c11` and `/std:c17`](https://learn.microsoft.com/en-us/cpp/build/reference/std-specify-language-standard-version?view=msvc-170) switches.
  * Additional STL improvements include full support for [`std::reverse_copy`](https://learn.microsoft.com/en-us/cpp/standard-library/algorithm-functions?view=msvc-170#reverse_copy), and more.
  * Upgraded version of CMake shipped with Visual Studio to
  * Our code analysis tools now support the SARIF 2.1 standard: the industry standard static analysis log format.
  * Missing build tools in Linux projects will now issue a warning in the toolbar and a clear description of the missing tools in the error list.
  * You can now debug Linux core dumps on a remote Linux system or WSL directly from Visual Studio.
  * For C++ Doxygen comment generation, we added additional comment style options (`/*!` and `//!`).
  * Additional
  * Compiler support for lambdas in unevaluated contexts.
  * [`/DEBUG:FULL`](https://learn.microsoft.com/en-us/cpp/build/reference/debug-generate-debug-info?view=msvc-170) link performance improved by multi-threading PDB creation. Several large applications and AAA games see between 2 to 4 times faster linking.
  * The Visual Studio debugger now has support for **`char8_t`**.
  * Support for ARM64 projects using clang-cl.


[](https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-cpp-2019?view=msvc-170&source=recommendations#whats-new-for-c-in-visual-studio-version-167)
